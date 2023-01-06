from collections import deque
import random

# A deque (double-ended queue) is represented internally as a doubly linked list. 
# (Well, a list of arrays rather than objects, for greater efficiency.) Both ends are accessible, 
# but even looking at the middle is slow, and adding to or removing from the middle is slower still. 

def move_queue(steps):
    queue = deque([i for i in range(100)])
    for i in range(steps):
        queue.appendleft(random.randint(0, 99))
        queue.pop()
    print(queue)

move_queue(steps=100)