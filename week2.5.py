math = [
    ('3+2', 5, 3),
    ('5÷2의 몫', 2, 5),
    ('10-2', 8, 3),
    ('10^2×2', 200, 5),
    ('1-(10÷4의 나머지)', -1, 5),
    ('2^4', 16, 3),
    ('4÷2', 2, 3)
]

ansCnt, wroCnt, tot = 0, 0, 0

for i in math:
    print("문제: %s" % i[0])
    ans = int(input("정답을 입력하세요! "))
    if ans == i[1]:
        ansCnt += 1
        tot += i[2]
    else:
        wroCnt += 1

print("-" * 30)
print("정답 개수: %d" % ansCnt)
print("오답 개수: %d" % wroCnt)
print("Total Score: %d" % tot)
print("-" * 30)
