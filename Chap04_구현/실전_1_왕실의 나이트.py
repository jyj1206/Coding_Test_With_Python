cur = input()

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

x = int(cur[1])
y = ord(cur[0]) - ord('a') + 1 

cnt = 0
for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]
  if 1 <= nx <= 8 and 1 <= ny <= 8:
    cnt += 1
    
print(cnt)