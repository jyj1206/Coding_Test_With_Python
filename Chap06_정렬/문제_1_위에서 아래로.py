n = int((input()))

array = [int(input()) for _ in range(n)]

result = sorted(array, reverse=True)

print(*result)
