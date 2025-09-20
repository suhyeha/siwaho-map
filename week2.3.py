def gcd(a, b):  # 예: 60, 28
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

print("최대공약수: %d" % gcd(60, 28))