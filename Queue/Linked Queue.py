class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedQueue:
    def __init__(self):
        self.front = ''
        self.rear = ''
        self.qCount = 0

    def isEmpty(self):
        return True if self.front == '' else False  
    
    def qSize(self):
        return self.qCount

    def enqueue(self,data):
        node = Node(data)

        if self.front == '':
            self.front, self.rear = node, node
             
        else:
            self.rear.next = node
            self.rear = node
        self.qCount += 1

    def dequeue(self):
        front = self.front
        
        if front == '':
            print("Delete Error(Empty)!!")
            return 

        if self.front == self.rear:
            self.rear, self.front = '', ''
        else:
            self.front = self.front.next
            del front

        self.qCount -=1 

    def printQueue(self):
        front = self.front

        if front == '':
            print("Queue is Empty!!")
            return 
        
        print("Linked Queue : [",end = ' ')
        while front:
            print(front.data,end=' <- ')
            front = front.next
        print("x]")


if __name__ == "__main__":
    que = linkedQueue()

    while True:
        print("==========Linked Queue Test!!============")
        print("1. enqueue")
        print("2. dequeue")
        print("3. Queue size?")
        print("4. imEmpty?")
        print("5. printQueue")
        print("6. exit")

        n = int(input())

        if n == 1:
            data = int(input("Data 입력 : "))
            que.enqueue(data)
            que.printQueue()
        elif n == 2:
            que.dequeue()
            que.printQueue()
        elif n == 3:
            print("Queue size = ",que.qSize())
        elif n == 4:
            print("Empty? = ",que.isEmpty())
        elif n == 5:
            que.printQueue()
        elif n == 6:
            break