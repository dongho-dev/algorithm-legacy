import sys
import heapq

# 입력 처리
n, m = map(int, sys.stdin.readline().strip().split())
card = list(map(int, sys.stdin.readline().strip().split()))

# 합체 처리
minHeap = []
minimum = 0

for i in card:
    heapq.heappush(minHeap, i)

for _ in range(m):
    first = heapq.heappop(minHeap)
    second = heapq.heappop(minHeap)
    sum = first + second
    heapq.heappush(minHeap, sum)
    heapq.heappush(minHeap, sum)

for i in minHeap:
    minimum += i

# 출력 처리
print(minimum)