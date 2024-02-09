n = int(input())

array = [input().split() for _ in range(n)]

result = sorted(array, key = lambda x : int(x[1]))

for name, _ in result:
  print(name, end = ' ')
