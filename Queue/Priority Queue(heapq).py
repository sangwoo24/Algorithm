import heapq

heap = []
heapq.heappush(heap,(2,"minju"))
heapq.heappush(heap,(6,"junza"))
heapq.heappush(heap,(1,"sangwoo"))

print(heap)
print(heapq.heappop(heap))