n, m = map(int, input().split())
box = [0] * n #n개 박스 0 으로 리스트 초기화
for _ in range(m): #m번 반복
    i, j, k = map(int, input().split())
    for a in range(i-1, j):
        box[a] = k

#print(box) 리스크 형식으로 나옴
print(*box)