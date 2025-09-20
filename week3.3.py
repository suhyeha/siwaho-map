def factorial(n):
    if n==1: return 1
    else: return n* factorial(n-1)

def factorial2(n):
    result=1
    for k in range(n,0,-1):
        result*=k
    return result


print("팩토리얼(순환)= ",factorial(3))
print("팩토리얼(반복)= ",factorial2(3))