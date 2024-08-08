a, b = map(int, input().split())
c = int(input())

new_time  = a*60 + b + c


new_h = (new_time//60)%24
new_m = new_time%60

print(new_h, new_m)