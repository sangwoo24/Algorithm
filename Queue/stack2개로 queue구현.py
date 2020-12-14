
class Queue:
    def __init__(self):
        self.pop_stack = []
        self.push_stack = []

    def enqueue(self,data):
        self.push_stack.append(data)

    def dequeue(self):
        if not self.push_stack and not self.pop_stack:
            print("Stack empty")
            return 

        if not self.pop_stack:
            for i in range(len(self.push_stack)):
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def printStack(self):
        print("push : ", self.push_stack)
        print("pop : ",self.pop_stack)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue.dequeue()
    queue.dequeue()
    queue.printStack()

