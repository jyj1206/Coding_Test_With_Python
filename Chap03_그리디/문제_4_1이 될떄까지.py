n, k = map(int, input().split())
result = 0

while True:
  # 현재 값에서 k로 나누어떨어지는 n 보다 작은 가장 큰 k 찾기
  target = (n // k) * k
  result += (n - target)
  n = target

  if n < k:
    break
    
  # k로 나누기 
  result += 1
  n //= k

result -= 1
print(result)