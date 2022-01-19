import os
import random
import re
import sys
import math

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    probability_distribution = {}  # Creating empty dictionary to store probability distribution.
    for link in corpus[page]:
        probability_distribution[link] = 0  # Setting initial value to 0

    if len(probability_distribution) != 0:
        random_factor = (1 / len(corpus)) * (1 - damping_factor)  # 1/pages * (1-d)
        follow_factor = (1 / len(probability_distribution)) * damping_factor + random_factor  # (1/links) *0,85 + rf

        for link in corpus[page]:
            probability_distribution[link] = follow_factor
        for site in corpus.keys():
            if site not in probability_distribution:
                probability_distribution[site] = random_factor
    # if the site has no links (or no links other than recursive links to the site)
    else:
        random_factor = (1 / len(corpus))  # then we should chose any random site from the corpis with
        # equal probability
        for site in corpus.keys():
            probability_distribution[site] = random_factor

    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    PageRank_vis = {}  # initiating empty dictionary.
    for site in corpus.keys():
        PageRank_vis[site] = 0

    page = random.choice(list(corpus))  # chosing random page that would not count as an entry

    v = 0
    for v in range(n):
        follow_page_prop_distr = transition_model(corpus, page, DAMPING)
        keys = []
        probs = []
        for site in follow_page_prop_distr:
            keys.append(site)
            probs.append(follow_page_prop_distr[site])
        page = random.choices(keys, weights=probs, k=1)[0]
        PageRank_vis[page] += 1

    PageRank = {}
    for site in PageRank_vis:
        PageRank[site] = PageRank_vis[site] / n

    return PageRank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    change_flag = True

    PageRank_pop = {}  # initiating empty dictionary.
    for site in corpus.keys():
        PageRank_pop[site] = 1 / len(corpus)

    # A page that has no links
    # at all should be interpreted as having one link for every page in the corpus (including itself).
    for am_links in corpus:
        if len(corpus[am_links]) == 0:
            ad_list = set()
            for ad_link in corpus:
                if am_links != ad_link:  # ?TODO? If not passed, rethink this line.
                    ad_list.add(ad_link)
            corpus[am_links] = ad_list

    change_flag = True

    while change_flag == True:
        change_flag = False
        PageRank_pop_new = {}

        for site in corpus:
            # Implementation of d(E[i] PR(i) / NumLinks(i)).
            PR_i = 0
            ref_links = []

            # Searches for very reference to the site (reference by link)
            for link in corpus:
                if link == site:
                    pass
                elif site in corpus[link]:
                    ref_links.append(link)

            # Calcuates the weight based on the PR of sites.
            for link in ref_links:
                PR_i += PageRank_pop[link] / len(corpus[link])
                # Implementation of full Iterative Algorithm equation.
            PageRank_pop_new[site] = ((1 - damping_factor) / len(corpus)) + (damping_factor * PR_i)

            convergence_factor = math.fabs(PageRank_pop[site] - PageRank_pop_new[site])
            if convergence_factor > 0.001:
                change_flag = True
        for site in PageRank_pop_new:
            PageRank_pop[site] = PageRank_pop_new[site]

    return PageRank_pop


if __name__ == "__main__":
    main()
