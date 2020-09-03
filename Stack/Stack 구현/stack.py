import sys

class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            return '-1'
        else:
            return self.items.pop()
    def isEmpty(self):
        if len(self.items) == 0:
            return '1'
        else:
            return '0'
    def size(self):
        return len(self.items)
    def top(self):
        if len(self.items) == 0:
            return '-1'
        else:
            return self.items[len(self.items)-1]
        

stk = stack()   
n = int(input())

for i in range(n):
    str = sys.stdin.readline().rstrip()
    if str[0:4] == "push":
        num = int(str[4:])
        stk.push(num)
    elif str == "pop":
        print(stk.pop())
    elif str == "empty":
        print(stk.isEmpty())
    elif str == "size":
        print(stk.size())
    elif str == "top":
        print(stk.top())
        
