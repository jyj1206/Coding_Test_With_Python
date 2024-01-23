n, m, k = map(int, input().split())

# 입력 값을 큰수부터 정렬
arr = sorted(list(map(int, input().split())))

first = arr[-1]
second = arr[-2]

second_count = m // (k + 1)
first_count = m - second_count

result = first * first_count + second_count * second

print(result)