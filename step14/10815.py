import bisect

n = int(input())
card = list(map(int, input().split()))
m = int(input())
card2 = list(map(int))
card.sort()
answer = [0] * m
for o in card2:
    l = bisect.bisect_left(card, o)
    r = bisect.bisect_right(card, o)
    print(r - l, end=' ')