n, m = map(int, input().split())
box = [0] *n
for i in range(n):
    box[i] = i+1 #인덱스는 0번부터 시작함

for _ in range(m):
    a, b = map(int, input().split())
    box[a-1], box[b-1] = box[b-1], box[a-1] # a, b = b, a 서로 형식 바꾸기

#print(box) 리스ㅌ 형식으로 나옴
print(*box) #리스트 안에 요소로 출력하는 형식