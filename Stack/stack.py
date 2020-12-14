class stack:
    def __init__(self):
        self.item = []
    
    def push(self,item):
        self.item.append(item)
    
    def pop(self):
        if not self.isEmpty:
            return self.item.pop()
        else:
            print("empty!!")
    
    def size(self):
        return len(self.item)

    def isEmpty(self):
        return False if self.item else True
    
    def printStack(self):
        for i in self.item:
            print(i)

if __name__ == "__main__":
    stack = stack()
    stack.pop()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.printStack()