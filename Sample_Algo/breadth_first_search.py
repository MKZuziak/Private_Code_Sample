from collections import deque
import random

def bfs(graph, searched_element, starting_point=0):
    search_queue = deque()
    search_queue += graph[starting_point]
    searched = []
    while search_queue:
        element = search_queue.popleft()
        if element not in searched:
            if element == searched_element:
                print('Element {} found'.format(element))
                return True
            else:
                search_queue += graph[element]
                searched.append(element)
    print("Element {} is not in the graph or can be reached from the starting point".format(searched_element))
    return False

def graph_maker(elements_no=10, directed = True):
    elements = [i for i in range(elements_no)]
    graph = {element: list() for element in elements}
    for element in elements:
        graph[element] = list()
        number_of_connections = random.randint(0, (elements_no-1))
        for _ in range(number_of_connections):
            new_con_no = random.randint(0, (elements_no-1))
            if elements[new_con_no] not in graph[element] and new_con_no != element:
                graph[element].append(elements[new_con_no])
                if directed == True:
                    if element not in graph[new_con_no]:
                        graph[new_con_no].append(element)
    return graph

while True:
    graph = graph_maker(elements_no=4)
    result = bfs(graph, searched_element=2, starting_point=3)
    if result == False:
        print(graph)
        break