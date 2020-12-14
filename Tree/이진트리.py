#이진 트리 : 최대 branch의 갯수가 2개
#이진 탐색 트리 : 이진 트리에서 조건이 붙혀짐
class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
#이진 탐색 트리
class Tree():
    def __init__(self,head):
        self.head = head #root노드

    
    def insert(self,value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value: 
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    
    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self,data):
        searched = False
        self.current_node = self.head
        self.parent_node = self.head

        while self.current_node:
            if self.current_node.value == data:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent_node = self.current_node       #부모도 바꿔줘야함
                self.current_node = self.current_node.left
            else:
                self.parent_node = self.current_node
                self.current_node = self.current_node.right
        if searched == False:
            return False
        
        #case1 - 단말노드
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent_node.value:
                self.parent_node.left = None
            else:
                self.parent_node.right = None
            del self.current_node   #객체가 메모리 상에서 지워짐
        
        #case2-1 - 삭제할 노드가 한개의 자식이 있을 경우(왼쪽 자식)
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent_node.value:
                self.parent_node.left = self.current_node.left
            else:
                self.parent_node.right = self.current_node.left
        
        #case2-2 삭제할 노드가 한개의 자식이 있을 경우(오른쪽 자식)
        if self.current_node.left == None and self.current_node.right != None:
            if value < self.parent_node.value:
                self.parent_node.left = self.current_node.right
            else:
                self.parent_node.right = self.current_node.right
        

        #case3 삭제할 노드가 두개의 자식 모두를 가지고 있을 때 (삭제할 노드가 왼쪽일 경우)
        if self.current_node.left != None and self.current_node.right != None:
            if value < self.parent_node.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.change_node.right # -> current_node_right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                
                self.parent_node.left = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right


        #case4 삭제할 노드가 두개의 자식 모두를 가지고 있을 때 (삭제할 노드가 오른쪽일 경우)
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left

                if self.change_node.right:
                    self.change_node_parent.left = self.change_node.right 
                else:
                    self.change_node_parent.left = None
                    
                self.parent_node.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
        
if __name__ == "__main__":
    rootNode = Node(8)
    tree1 = Tree(rootNode)
    tree1.insert(5)
    tree1.insert(10)
    tree1.insert(2)
    tree1.insert(1)
    tree1.insert(3)
    tree1.insert(6)
    tree1.insert(7)
    
    print(tree1.search(8))