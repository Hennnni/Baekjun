num = [int(input()) for _ in range(10)]
#ans = [] #중복제거가 안됨
ans = set()

for n in num:
    ans.add(n %42)

print(len(ans))