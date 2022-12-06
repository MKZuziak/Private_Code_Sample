import string
from collections import Counter
#letters_used = [letter for letter in string.ascii_lowercase]
def detect_packet(source):
    char_list = list()
    chars_used = 0
    unique_chars = 0
    with open(source) as file:
        for line in file:
            for char in line:
                chars_used += 1
                if char not in char_list:
                    char_list.append(char)
                    unique_chars += 1
                    if unique_chars == 4:
                        return chars_used
                else:
                    char_list.append(char)
                    count_list = Counter(char_list)
                    while count_list[char] != 1:
                        char_list = char_list[1:]
                        count_list = Counter(char_list)
                    unique_chars = len(char_list)


source = 'Day 6\source.txt'
packet = detect_packet(source)
print(packet)