from collections import deque

#DFS

class Search():
    def __init__(self,graph,first_node):
        self.graph = graph
        self.first_node = first_node
    
    #stack1, queue1
    def dfs(self):
        visited_queue, need_to_visit = deque(), deque()
        need_to_visit.append(self.first_node)

        while need_to_visit:
            check_node = need_to_visit.pop()
            if check_node not in visited_queue:
                visited_queue.append(check_node)
                need_to_visit.extend(self.graph[check_node])
        return visited_queue

    def bfs(self):
        visited_queue, need_to_visit = deque(), deque()
        need_to_visit.append(self.first_node)
        
        while need_to_visit:
            check_node = need_to_visit.popleft()
            
            #if check_node not in visited_queue:
            if visited_queue.count(check_node) == 0:
                visited_queue.append(check_node)
                need_to_visit.extend(self.graph[check_node])
        return visited_queue

if __name__ == "__main__":
    graph = dict()
    graph['A'] = ['B','C']
    graph['B'] = ['A','D']
    graph['C'] = ['A','G','H','I']
    graph['D'] = ['B','E','F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C','J']
    graph['J'] = ['I']

    search1 = Search(graph,'A')
    print("dfs",search1.dfs())
    print("bfs",search1.bfs())