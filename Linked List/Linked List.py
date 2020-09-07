#모듈이름은 소문자 + 밑줄로 구성
#Class는 첫 단어에 대문자로 구성

#node의 주소를 알아야 하므로 class로 선언해주는 것 같음.
class Node():
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self,data):
        firstNode = Node(data)
        self.head = firstNode
    
    #Linked list 맨 뒤 원소추가
    def append(self,data):
        new_node = Node(data)
        head = self.head
        if head == '':
            head = new_node
        while head.next:
            head = head.next
        head.next = new_node

    #Linked List 원소출력
    def print_list(self):
        head = self.head
        while head:
            print(head.data)
            head = head.next

    #Linked List 특정 원소 뒤에 삽입
    def insert(self,current_data,insert_data):
        new_node = Node(insert_data)
        head = self.head
        while head.data != current_data:
            head = head.next
        temp = head.next
        head.next = new_node
        new_node.next = temp
    
    #Linked List 맨 앞 원소 삭제
    def delete_front(self):
        head = self.head
        if head == '':
            print('삭제할 원소가 없습니다.')
            return False
        if self.head.next:
            self.head = self.head.next
            del head
        else:
            self.head = ''

    #Linked List 특정 원소 삭제
    def pop(self,data):
        head = self.head

        if head == '':
            print('삭제할 원소가 없습니다.')
            return
        
        if head.data == data:
            self.head = self.head.next
            del head
            return
        while head.next.data != data:
            head = head.next
        temp = head.next
        head.next = temp.next

    #Linked list 특정 원소 뒤에 원소추가  -> 특정 원소가 list 안에 없으면?
    def insert(self,stored_data,new_data):
        new_node = Node(new_data)
        head = self.head

        while head.data != stored_data:
            head = head.next
            if head == None:
                print("찾는 원소가 없습니다")
                return False
        new_node.next = head.next
        head.next = new_node

    def print_linked_list(self):
        head = self.head
        while head:
            print("LinkedList에 존재하는 노드는 : ",head.data)
            head = head.next
    
    #Linked list 원소 삭제 
    def delete(self,data):
        head = self.head
        if head == '':
            print("삭제할 원소가 없습니다")
            return False
        if head.data == data:
            self.head = None
            del head
            return True
        
        while (head.next != None) and (head.next.data != data):
            head = head.next
            if head == None:
                print("찾는 원소가 없습니다")
        temp = head.next
        head.next = head.next.next
        del temp


if __name__ == "__main__":
    linkedList1 = LinkedList()
    for i in range(1,4):
        linkedList1.append(i)
    linkedList1.print_list()
    linkedList1.pop(2)
    linkedList1.print_list()


if __name__ ==  "__main__":
    linkedList1 = LinkedList(0)
    linkedList1 = LinkedList(0)
    linkedList1.print_linked_list()

# self.data = 0 , self.next = None -> self.data의 주소를 알아야함.

'''
class Node():
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoubleLinkedList():
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head

    #Double Linked List 맨 앞부터 원소출력
    def print_list_front(self):
        head = self.head
        while head:
            print("맨 앞부터 List 원소 출력 : ",head.data,"-------Prev : ",head.prev, "Next : ",head.next)
            if head.prev != None:
                print("이전 data : ",head.prev.data)
            if head.next != None:
                print("앞 data : ", head.next.data)
            head = head.next

    def append(self,data):
        new_node = Node(data)
        head = self.head
        if head == '':
            head = new_node
        while head.next:
            head = head.next
        new_node.prev = head
        head.next = new_node
        self.tail = new_node
    
    #Double Linked List 특정 원소 뒤에 삽입
    def insert(self,stored_data,new_data):
        tail = self.tail

        while tail.data != stored_data:
            tail = tail.prev
            if tail == None:
                print("찾는 원소가 없음")
                return False
        new_node = Node(new_data)
        if tail.next != None:
            tail.next.prev = new_node
        else:
            self.tail = new_node
        new_node.next = tail.next
        tail.next = new_node
        new_node.prev = tail
    

    def delete(self,data):
        head = self.head

        if head == '':
            print("지울 노드가 없습니다")
            return False
        
        if head.data == data:
            self.head = head.next
            del head

        while head.data != data:
            head = head.next
            if head == None:
                print("찾는 원소가 없습니다")
                return False
        head.prev.next = head.next
        head.next.prev = head.prev
        del head

    def delete(self,data):
        head = self.head
        if head == '':
            print("삭제할 노드가 없습니다") 
            return False
        if head.data == data:
            self.head = head.next
            if head.next:
                head.next.prev = None
            del head
            return True
        while head.data != data:
            head = head.next

        if head.next == None:
            head.prev.next = head.next
        else:
            head.prev.next = head.next
            head.next.prev = head.prev
        del head

if __name__ == "__main__":
    doubleLinkedList1 = DoubleLinkedList(0)
    doubleLinkedList1.append(1)
    doubleLinkedList1.append(2)
    doubleLinkedList1.append(3)

    doubleLinkedList1.delete(0)
    doubleLinkedList1.print_list_front()
'''
