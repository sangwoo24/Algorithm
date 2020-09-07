#모듈이름은 소문자 + 밑줄로 구성
#Class는 첫 단어에 대문자로 구성
'''
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList():
    #생성자
    def __init__(self):
        firstNode = Node('first')
        self.head = firstNode

    #Linked List append - 맨 뒤에 원소 삽입
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
        del temp


if __name__ == "__main__":
    linkedList1 = LinkedList()
    for i in range(1,4):
        linkedList1.append(i)
    linkedList1.print_list()
    linkedList1.pop(2)
    linkedList1.print_list()
'''



class LinkedList():
    def __init__(self,data):
        print(self.create_node(data))


    def create_node(self,data,next = None):
        self.data = data
        self.next = next
    
    def print_list(self):
        head = self.head
        while head:
            print(head.data)
            head = head.next

if __name__ ==  "__main__":
    linkedList1 = LinkedList(0)









