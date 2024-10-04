while True:
    n, m = map(int, input().split())
       
    if m == 0 and n == 0:
        break
    else:
            
        if m%n==0:
            print("factor")
        elif n%m==0:
            print("muliple")
        else: print("neither")