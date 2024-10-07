import bisect

N = int(input())
card = list(map(int, input().split()))
M = int(input())
card2 =  list(map(int, input().split()))

n_dic = {}
for n in card:
    if n in n_dic:
        n_dic[n] += 1
    else: n_dic[n] = 1

def bin(m, card, start, end):
    if start > end:
        return 0
    mid = (start + end)//2
    
    if m == card[mid]:
        return n_dic[m]
    elif m<card[mid]: return bin(m, card, start, mid-1)
    else: return bin(m, card, mid+1, end)

for m in card2:
  print(bin(m, card, 0, len(card)-1), end=' ')