import random

def binary_search(lst,search_data):
    print(lst)
    
    if len(lst) == 1 and lst[0] == search_data:
        return True
    elif len(lst) == 0:
        return False
    index = len(lst) // 2

    if lst[index] == search_data:
        return True
    else:
        if search_data > lst[index]:
            return binary_search(lst[index + 1 :],search_data)
        else:
            return binary_search(lst[:index],search_data)
    
if __name__ == "__main__":
    lst = random.sample(range(1, 100), 10)
    print(binary_search(sorted(lst),10)) 