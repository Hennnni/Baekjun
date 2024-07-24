a = int(input())
b = int(input())

b1 = b % 10 #일의자리
b2 = (b // 10)%10 #십의자리
b3 = b//100 # 백의자리

print(a * b1)
print(a * b2)
print(a * b3)
print(a * b)