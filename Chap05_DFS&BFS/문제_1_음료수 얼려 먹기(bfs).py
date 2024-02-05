from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
  q = deque([(x, y)])
  
  # 방문 처리
  graph[x][y] = 1
  
  while q:
    x, y = q.popleft()
    
    # 네 방향 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 얼음 틀이 벗어나는지 확인
      if 0 <= nx < n and 0 <= ny < m:
        # 칸막이가 아니면서 방문하지 않았으면
        if graph[nx][ny] != 1:
          graph[nx][ny] = 1
          q.append((nx, ny))

result = 0

for i in range(n):
  for j in range(m):
    # 한번도 방문하지 않은 경우(시작점)
    if graph[i][j] != 1:
      bfs(i, j)
      # 아이스크림 개수 1 증가
      result += 1

print(result)