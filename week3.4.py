def hanoi_tower(n, fr, tmp, to):
    if n == 1:
        print(" 원판1: %s -> %s" % (fr, to))
    else:
        hanoi_tower(n - 1, fr, to, tmp)          # 1단계: n-1개를 임시 기둥으로 이동
        print(" 원판%d: %s -> %s" % (n, fr, to))  # 2단계: 가장 큰 원판 이동
        hanoi_tower(n - 1, tmp, fr, to)          # 3단계: n-1개를 목표 기둥으로 이동

# 함수 호출 (n=3)
hanoi_tower(4, "A", "B", "C")


