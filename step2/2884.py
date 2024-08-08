# 분, 초 받기
H, M = map(int, input().split())
def solution(H, M):
    time = H * 60 + M
    new_time = time - 45

    
    # 만약 음수라면, 전날로 돌아가기
    if new_time< 0:
        new_time += 24 * 60

    #새로운 시, 분 구하기
    newH = new_time//60
    newM = new_time%60

    return newH, newM

newH, newM = solution(H, M) #여기서 안받아주면 RETURN 안에 있어도 밖에서 못가져옴
print(newH, newM)