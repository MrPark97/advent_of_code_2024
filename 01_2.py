import sys
import heapq

list_a = []
dict_b = {}

with open('input/01.txt', 'r') as file:
    for line in file:
        a, b = map(int, line.split())
        list_a.append(a)
        dict_b[b] = dict_b.get(b, 0) + 1

similarity = 0

for a in list_a:
    similarity += a * dict_b.get(a, 0)

print(similarity)