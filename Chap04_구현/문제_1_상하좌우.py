n = int(input())
arr = input().split()

# 방향에 따라 x, y 좌표 이동 정도를 나타내는 dict 선언
directions = {'L':(0, -1), 'R':(0, 1), 'U':(-1, 0), 'D':(1, 0)}

x, y = 1, 1

# 이동
for d in arr:
  dx, dy = directions[d]
  nx = x + dx
  ny = y + dy
  if 1 <= nx <= n and 1 <= ny <= n :
    x, y = nx, ny

print(x, y) 