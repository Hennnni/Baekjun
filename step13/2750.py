n = int(input())
result = []
for i in range(n):
    result.append(int(input()))

print("\n".join(map(str,sorted(result))))