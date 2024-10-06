import sys
n = int(input())
result = []
for i in range(n):
    result.append(int(sys.stdin.readline()))

print("\n".join(map(str,sorted(result))))