import sys
from collections import deque


def isIndexError(row,column):
    if row >= height or row < 0 or column >= width or column < 0:
        return False
    return True

def bfs(graph,row,column):
    que = deque([[row,column]])
    visit = []


if __name__ == "__main__":
    height, width = list(map(int,sys.stdin.readline().split()))

    graph = []
    for i in range(height):
        row = list(map(int,sys.stdin.readline().rstrip()))
        graph.append(row)

    bfs(graph,0,0)

