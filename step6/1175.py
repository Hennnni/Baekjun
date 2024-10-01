word = input().upper() #대문자로 출력해줌

a = {}
#빈도새기
for char in word:
    if char in a:
        a[char] +=1
    else: a[char]=1

max_count = max(a.values())
print(max_count)

most_frequent = [key for key, value in a.items() if value == max_count]


if len(most_frequent) > 1:
    print("?")
else:
    print(most_frequent[0])