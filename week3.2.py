import time
import random

def seq_search(A, key):
    for i in range(len(A)):
        if A[i] == key:  # ← 여기 수정
            return i
    return -1

num = list(range(1, 1001))
num2 = [random.randint(1, 1000) for _ in range(1001)]

REPEATS = 1000

# 1 찾는 시간
start = time.time()
for _ in range(REPEATS):
    seq_search(num, 1)
end = time.time()
t1 = end - start

# 1000 찾는 시간
start = time.time()
for _ in range(REPEATS):
    seq_search(num, 1000)
end = time.time()
t2 = end - start

print("1찾기 시간: ", t1)
print("1000찾기 시간: ", t2)

# 실제 위치 확인도 하고 싶으면 이렇게
print("1 위치:", seq_search(num, 1))
print("1000 위치:", seq_search(num, 1000))

