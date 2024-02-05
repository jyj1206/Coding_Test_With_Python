from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
  q = deque([(x, y)])
  
  while q:
    x, y = q.popleft()
    
    # 종료조건 : 목적지에 도착하면
    if x == n-1 and y == m-1:
        return graph[n-1][m-1]
    
    # 네 방향 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      # 미로 공간을 벗어나지 않았는지 확인
      if 0 <= nx < n and 0 <= ny < m:
        # 괴물이 있는 경우
        if graph[nx][ny] == 0:
          continue
        # 괴물이 없으면서 해당 노드를 처음 방문하는 경우(최단 경로)
        elif graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          q.append((nx, ny))

print(bfs(0, 0))