def gcd(a, b):  # 예: 60, 28
    alist = []
    for i in range(1, a+1):
        if a % i == 0:
            alist.append(i)
    print(alist, "\n")

    blist = []
    for i in range(1, b+1):
        if b % i == 0:   # 수정됨
            blist.append(i)
    print(blist, "\n")

    clist = []
    for i in alist:
        if i in blist:
            clist.append(i)
  

    return max(clist)

print(gcd(60, 28))






