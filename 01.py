import sys
import heapq

heap_a, heap_b = [], []

with open('input/01.txt', 'r') as file:
    for line in file:
        a, b = map(int, line.split())
        heapq.heappush(heap_a, -a)
        heapq.heappush(heap_b, -b)

distance = 0
n = len(heap_a)

for i in range(n):
    a, b = heapq.heappop(heap_a), heapq.heappop(heap_b)
    distance += abs((-a) - (-b))

print(distance)