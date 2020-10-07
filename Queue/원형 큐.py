class circularQueue:
    def __init__(self,max_size):
        self.rear = 0
        self.front = 0
        self.max = max_size
        self.que = [None for i in range(self.max)]

    def isEmpty(self):
        return True if self.rear == self.front else False
        
    def isFull(self):
        return True if (self.rear + 1) % self.max == self.front else False

    def enqueue(self,data):
        if self.isFull():
            print("is Full!! ")
        else:
            self.rear = (self.rear + 1) % self.max
            self.que[self.rear] = data

    def dequeue(self):
        if self.isEmpty():
            print("is Empty!!")
        else:
            self.front = (self.front + 1) % self.max
            return self.que[self.front]

    def printQueue(self):
        front = self.front
        rear = (self.rear + 1) % self.max

        while (front + 1) % self.max != rear: 
            front = (front + 1) % self.max
            print(self.que[front],end='')
        print(" ")


if __name__ == "__main__":
    queue = circularQueue(5)
    for i in range(4):
        queue.enqueue(i)
        queue.printQueue()

    for i in range(4):
        queue.dequeue()
        queue.printQueue()