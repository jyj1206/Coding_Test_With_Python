n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 오름 차순 정렬
a.sort()

# 내림 차순 정렬
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

# 모든 원소의 합 최대값 출력
print(sum(a))