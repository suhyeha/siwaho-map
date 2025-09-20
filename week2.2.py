def gcd(a, b):  # 예: 60, 28
    alist = []
    for i in range(1, a + 1):
        if a % i == 0:
            alist.append(i)
    print(alist, "\n")

    blist = []
    for i in range(1, b + 1):
        if b % i == 0:  # 수정됨
            blist.append(i)
    print(blist, "\n")

    for i in range(len(alist)-1,-1,-1):
        if alist[i] in blist:
            return alist[i]

print("최대공약수: %d" % gcd(60, 28))
