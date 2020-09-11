def dfs(graph,start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

def bfs(graph,start_node): #graph는 노드와 간선에 대한 dict
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node]) #node는 key임
    return visited


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

    print("BFS : " , bfs(graph,'A'))
    print("DFS : " , dfs(graph,'A'))