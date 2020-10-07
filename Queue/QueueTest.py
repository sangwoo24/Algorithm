from collections import deque
from queue import Queue
# list
queue = [1,2,3]

queue.append(4)
queue.append(5)

print(queue)

queue.pop(0)
queue.pop(0)
print(queue)

# deque
deque = deque([1,2,3])
deque.append(4)
deque.appendleft(0)
print(deque)

deque.pop()
deque.popleft()
print(deque)

# Queue
que = Queue()
que.put(1)
que.put(2)
que.put(3)

print(que.get())
print(que.get())
print(que.get())


class MyQueue:
    def __init__(self):
        self.queue = []
    
    def push(self,value):
        self.queue.append(value)
    
    def pop(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def back(self):
        return self.queue[-1]

    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    myqueue = MyQueue()


