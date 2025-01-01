n, m = map(int, input().split())
l = list(map(int, input().split()))

result = [str(num) for num in l if num<m] #뒤에 리스트가 아니라 join형식으로 변환
print(" ".join(result)) 