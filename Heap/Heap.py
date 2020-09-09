#완전 이진 트리 : 자식은 무조건 두개 다 존재, Data가 채워질 때는 왼쪽부터 채워진다.
#힙은 필히 자식노드보다 크거나(Max Heap) 작다(Min Heap)
#힙의 Data를 삭제하는 경우는 Root Node를 삭제하는 경우밖에 없다.
#Heap은 보통 list로 표현한다.

#부모 노드 index = 자식 / 2
#왼쪽 자식 노드 = 부모 * 2 
#오른쪽 자식 노드 = 부모 * 2 + 1

'''
class Heap:
    def __init__(self,initial_data):
        self.heap = []
        self.heap.append(None)
        self.heap.append(initial_data)
    
    def move_up(self,inserted_index):   #자식이 부모보다 크다는 것을 증명하는 함수
        if inserted_index <= 1:         #root Node일 때 
            return False
        parent_index = inserted_index // 2
        if self.heap[inserted_index] > self.heap[parent_index]:
            return True
        else:
            return False

    def insert(self,data):
        if len(self.heap) == 0:
            self.heap.append(None)
            self.heap.append(initial_data)
            return True
        self.heap.append(data)

        inserted_index = len(self.heap) - 1
        while self.move_up(inserted_index):
            parent_index = inserted_index // 2
            self.heap[inserted_index], self.heap[parent_index] = self.heap[parent_index], self.heap[inserted_index] #Swap
            inserted_index = parent_index
        return True

    def move_down(self,pop_index):
        left_child_pop_index = pop_index * 2
        right_child_pop_index = pop_index * 2 + 1
         
        # case 1: 왼쪽 자식 노드도 없을 때
        if left_child_pop_index >= len(self.heap):
            return False
        
        # case 2 : 오른쪽 자식 노드만 없을 때
        elif right_child_pop_index >= len(self.heap):
            if self.heap[pop_index] < self.heap[left_child_pop_index]:
                return True
            else:
                return False
        
        # case 3 : 왼쪽 오른쪽 자식 모두 있을때
        else:
            if self.heap[left_child_pop_index] > self.heap[right_child_pop_index]:
                if self.heap[left_child_pop_index] > self.heap[pop_index]:
                    return True
                else:
                    return False
            else:
                if self.heap[right_child_pop_index] > self.heap[pop_index]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap) <= 1: #None만 있거나 None도 없는 공백일 때 
            return None
        
        return_data = self.heap[1] #맨 하위노드 덮어씌우면 되니까 삭제 안해도 됨.
        self.heap[1] = self.heap[-1]
        del self.heap[-1]

        pop_index = 1
        while self.move_down(pop_index):
            left_child_pop_index = pop_index * 2
            right_child_pop_index = pop_index * 2 + 1
            
  
            # case 2 : 오른쪽 자식 노드만 없을 때
            if right_child_pop_index >= len(self.heap):
                if self.heap[pop_index] < self.heap[left_child_pop_index]:
                    self.heap[pop_index],self.heap[left_child_pop_index] = self.heap[left_child_pop_index],self.heap[pop_index]
                    pop_index = left_child_pop_index
    
            # case 3 : 왼쪽 오른쪽 자식 모두 있을때
            else:
                if self.heap[left_child_pop_index] > self.heap[right_child_pop_index]:
                    if self.heap[left_child_pop_index] > self.heap[pop_index]:
                        self.heap[pop_index],self.heap[left_child_pop_index] = self.heap[left_child_pop_index],self.heap[pop_index]
                        pop_index = left_child_pop_index
                else:
                    if self.heap[right_child_pop_index] > self.heap[pop_index]:
                        self.heap[pop_index],self.heap[right_child_pop_index] = self.heap[right_child_pop_index],self.heap[pop_index]
                        pop_index = right_child_pop_index
        return return_data



if __name__ == "__main__":
    heap1 = Heap(15)
    heap1.insert(10)
    heap1.insert(8)
    heap1.insert(5)
    heap1.insert(4)
    heap1.insert(20)
    print(heap1.heap)
    print(heap1.pop())
'''

class Heap:
    def __init__(self,data):
        self.heap = []
        self.heap.append(None)
        self.heap.append(data)

    def insert_data(self,data):
        if len(self.heap) == 0:
            self.heap.append(None)
        self.heap.append(data)
        insert_index = len(self.heap) - 1
        parent_index = self.parent_index(insert_index)
        
        #새로 들어온 data의 부모가 있고, 부모가 data보다 작을 때 -> 위치 swap
        while parent_index != 0 and self.heap[insert_index] > self.heap[parent_index]:
            self.heap[insert_index],self.heap[parent_index] = self.heap[parent_index], self.heap[insert_index]
            insert_index = parent_index
            parent_index = self.parent_index(insert_index)

    def get_max_heap(self):
        return_data = self.heap[1]
        self.heap[1] = self.heap[len(self.heap) - 1]
        del self.heap[len(self.heap) - 1]
        new_index = 1


        if len(self.heap) <= 1:
            return False
        elif len(self.heap) == 2:
            return_data = self.heap[1]
            return return_data
        else:
            while True:
                right = self.right_child_index(new_index)
                left = self.left_child_index(new_index)
                if right <= len(self.heap) - 1: #둘 다 존재
                    if self.heap[left] > self.heap[right]:
                        if self.heap[left] > self.heap[new_index]:
                            self.heap[left], self.heap[new_index] = self.heap[new_index], self.heap[left]
                            new_index = left
                        else:
                            break
                    elif self.heap[left] < self.heap[right]:
                        if self.heap[right] > self.heap[new_index]:
                            self.heap[right], self.heap[new_index] = self.heap[new_index], self.heap[right]
                            new_index = right
                        else:
                            break
                    else:
                        break
                elif left == len(self.heap) - 1:
                    if self.heap[left] > self.heap[new_index]:
                        self.heap[left], self.heap[new_index] = self.heap[new_index], self.heap[left]
                        new_index = left
                    else:
                        break
                else:
                    break
                    
        
    def left_child_index(self,index):
        return index * 2

    def right_child_index(self,index):
        return (index * 2) + 1  

    def parent_index(self,index):
        return index // 2

if __name__ == "__main__":
    heap1 = Heap(12)
    heap1.insert_data(10)
    heap1.insert_data(8)
    heap1.insert_data(8)
    heap1.insert_data(5)
    heap1.insert_data(30)

    heap1.get_max_heap()
    print(heap1.heap)