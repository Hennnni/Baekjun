l = [int(input()) for _ in range(9)] # 엔터된 숫자 입력받아서 그 값을 정수로 입력받기


max = max(l)
max_value = l.index(max)+1
print(max)
print(max_value)