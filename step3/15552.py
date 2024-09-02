import sys
input = sys.stdin.readline

# 첫 줄에 테스트 케이스의 수 T를 입력받습니다.
t = int(input().strip())

results = []  # 모든 결과를 저장할 리스트
for _ in range(t):
    a, b = map(int, input().split())  # 각 테스트 케이스에 대해 두 정수 a, b를 입력받습니다.
    results.append(a + b)  # 두 수의 합을 결과 리스트에 추가합니다.

# 출력 단계에서 모든 결과를 한 번에 출력합니다.
sys.stdout.write('\n'.join(map(str, results)) + '\n')