n = int(input())

array = [input().split() for _ in range(n)]

# 0점 ~ 100점
counts = [[] for i in range(101)]

for name, score in array:
  counts[int(score)].append(name)

for count in counts:
  for name in count:
    print(name, end=' ')
3