from collections import deque

'''
1. deque() for stack && queue
 - for queue
  - q = deque()
  - q.append(1)
  - q.pop()

2. set() for being a set  # Set does not perserve the order of insertion
    a = set()
    a.add(1)
    x in a # if x is in a 
3. dict = {} for creating an empty dictionary
    key in dict.keys() # if key is in dict.key()
    dict[key] = 'some_value' # set or update value for key
    dict.pop(key, None) to remove a key

3.1 in python 3.7 dict is guranteeded to be ordered 

4. OrderedDict for LinkedHashMap O(1) for deleting while maintainig order
    od = OrderedDict()
    od.popitem() # FIFO 
    od.popitem(True) #FILO
    od.move_to_end() # move head to last (right)
    od.move_to_end(False) # move head to first (left)    

5. OrderedSet for LinkedHashSet O(1) for deleting while maintainig order 
 - You may use fromKeys() and the value is default to None
 - use {} 3.7 or OrderedSet with Value to None

'''

class Demo:
    def __init__(self) -> None:
        pass

    # deque in favor of list (double listed list)
    # deque need quicker append and pop operations from both the ends of the container, as deque provides an O(1)
    def deque_demo(self):
        queue = deque()
        # append to the end
        queue.append(1)
        # [1]
        
        # append to the left (first )
        queue.appendleft(0)
        # [0, 1]

        # pop the last element
        # 1 is popped 
        print(queue.pop())
        
        queue.append([3,4,5])
        # 0 is popped 
        print(queue.popleft())
        # left is 3,4,5
        print(queue)

    def stack_demo(self):
        stack = deque([1,2,3])
        stack.append(4)
        stack.append(5)        
        print("Demo Stack: ", stack)

        # when pop, LIFO
        # pop() is the right most element, the one inserted 
        while (stack):
            print(stack.pop())

    # FIFO queue
    def queue_demo(self):
        # note [] in init gives you a queue
        queue = deque([1,2,3])
        queue.append(4)
        queue.append(5)
        print("Demo Queue: ", queue) 

        # when pop, FIFO
        while (queue):
            # popleft() as the first one
            print(queue.popleft())


d = Demo()
# d.deque_demo()

d.stack_demo()

d.queue_demo()