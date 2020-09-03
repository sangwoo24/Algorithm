import sys

class queue:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            return '-1'
        else:
            return self.items.pop(0)
    def isEmpty(self):
        if len(self.items) == 0:
            return '1'
        else:
            return '0'
    def size(self):
        return len(self.items)
    def front(self):
        if len(self.items) == 0:
            print('-1')
        else:
            print(self.items[0])
    def back(self):
        if len(self.items) == 0:
            print('-1')
        else:
            print(self.items[len(self.items)-1])
        

q = queue()   
n = int(input())

for i in range(n):
    str = sys.stdin.readline().rstrip()
    
    if str[0:4] == "push":
        num = int(str[4:])
        q.push(num)
    elif str == "pop":
        print(q.pop())
    elif str == "empty":
        print(q.isEmpty())
    elif str == "size":
        print(q.size())
    elif str == "front":
        q.front()
    elif str == "back":
        q.back()

 
     

