import numpy as np
'''
class HashMap():
    def __init__(self):
        self.table = [0 for i in range(10)]
    
    def get_Hash_key(self,data):
        key = hash(data)
        key = key % 10
        return key

    def storage_data(self,key,value):
        hash_address = self.get_Hash_key(key)
        self.table[hash_address] = value

    def get_hash_data(self,key):
        hash_address = self.get_Hash_key(key)
        print("해당 key값의 value는 : ",self.table[hash_address])
    def print_table(self):
        print(self.table)

if __name__ == "__main__":
    hash1 = HashMap()
    hash1.storage_data('sangwoo',100)
    hash1.get_hash_data('sangwoo')
    '''



'''
#Hash Table 충돌 ->Chaning 기법 
#Key와 Data를 리스트 형태로 저장한 뒤, 충돌이 일어나게되면(같은 index값을 가지면) 해당 인덱스에 있는 자료를 Linked List로 만든 뒤 기존 Data뒤에 연결시킴.
class HashMap():
    def __init__(self):
        self.table = np.empty(10,dtype = object)
    
    def get_key(self,data):
        return hash(data)

    def hash_function(self,key):
        return key % 10
    
    def storage_data(self,data,value):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)
        
        if self.table[hash_address] != None:
            for index in range(len(self.table[hash_address])):
                if self.table[hash_address][index][0] == index_key:
                    self.table[hash_address][index][1] = value
                    return
            self.table[hash_address].append([index_key,value])
        else:
            self.table[hash_address] = [[index_key,value]]
    
    def get_data(self,data):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)

        if self.table[hash_address] != None:
            for index in range(len(self.table[hash_address])):
                if self.table[hash_address][index][0] == index_key:
                    return self.table[hash_address][index][1]
            return None
        else:
            return None

if __name__ == "__main__":
    hash1 = HashMap()
    hash1.storage_data('sangwoo',56962353)
    hash1.storage_data('minju',41033330)

    print(hash1.get_data('sangwoo'))
'''

#Hash Table 충돌 -> Linear Probing 기법
#충돌이 일어날 시 Table에 다음 index의 Data가 존재하는지 확인하여 존재하지 않는 index까지 이동 후 저장하는 기법.

class HashMap():
    def __init__(self):
        self.table = np.empty(10,dtype = object)
    
    def get_key(self,data):
        return hash(data)

    def hash_function(self,key):
        return key % 10

    def storage_data(self,data,value):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)
        
        if self.table[hash_address] != None:
            for index in range(hash_address,len(self.table)): #현재의 address부터 빈 공간이 있는지 확인하기 위해 
                if self.table[index] == None:
                    self.table[index] = [index_key,value] #각 table의 원소는 hash key와 value로 저장됨
                elif self.table[index][0] == index_key:
                    self.table[index][1] = value
                    return
        else:
            self.table[hash_address] = [index,value]

    #Linear Probing 기법은 충돌 시 address앞의 빈공간에 key와 value를 넣으므로 data를 읽을 때 hash_address이후의 data를 순회하면서 
    #자신이 원하는 key값이 있는지 확인해야한다.
    #Linear Probing기법은 동일한 Hash_Address일 경우 충돌 시 바로 다음칸이나 더 뒤의칸의 공백에 data가 들어가야하는데, 같은 hash_address를 
    #가질경우 순회하면서 공백이 발견됐다는 것은 해당하는 index_key의 value가 저장된 적이 없다는 소리임.
    def get_data(self,data):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)

        if self.table[hash_address] != None:
            for index in range(hash_address,len(self.table)): 
                if self.table[index] == None:
                    return None:
                elif self.table[index][0] == index_key:
                    return self.table[index][1]
        
        else:
            return None