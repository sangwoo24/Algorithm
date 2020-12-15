from collections import deque

def bfs(graph, startNode):
    visit, queue = deque(), deque(startNode)

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit


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
