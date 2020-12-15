# stack
def dfs_stack(startNode, visit = []):
    stack = [startNode]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit

# 재귀함수
def dfs_recursive(startNode, visit = []):
    visit.append(startNode)

    for i in graph[startNode]:
        if i not in visit:
            dfs_recursive(i)
    return visit

if __name__ == "__main__":
    graph = dict()
    graph = {
        '0': ['1'],
        '1': ['0', '2', '3'],
        '2': ['1', '4', '3'],
        '3': ['1', '2', '4', '5'],
        '4': ['2', '3'],
        '5': ['3', '6', '7'],
        '6': ['5', '8'],
        '7': ['5'],
        '8': ['6'],
    }

    print("DFS Stack: " , dfs_stack('0'))
    print("DFS Recursive: " , dfs_recursive('0'))
