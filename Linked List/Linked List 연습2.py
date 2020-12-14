class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,data):
        self.head = Node(data)

    def append(self,data):
        new_node = Node(data)
        head = self.head

        if head == '':
            head = new_node
        while head.next:
            head = head.next
        head.next = new_node
    
    def search(self,data):
        head = self.head

        while head:
            if head.data == data:
                print("exist")
            else:
                head = head.next
        print("there is no data in List")

    def printList(self):
        head = self.head

        while head:
            print("data : ", head.data)
            head = head.next
    
    def delete(self,data):
        head = self.head
        if head.data == data:
            head = None
            return
            
        while head.next:
            if head.next.data == data:
                temp = head.next
                head.next = head.next.next
                del temp
                print("delete")
                return
        print("no data")

if __name__ == "__main__":
    linkedList = LinkedList(10)
    linkedList.append(11)
    linkedList.append(12)
    linkedList.append(13)




    linkedList.delete(10)
    linkedList.printList()

