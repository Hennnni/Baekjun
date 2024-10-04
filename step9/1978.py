def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 입력
N = int(input())
numbers = map(int, input().split())

# 소수 개수 계산
prime_count = sum(1 for number in numbers if is_prime(number))

# 출력
print(prime_count)
