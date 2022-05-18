import time
import math


def mianJob(n):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(n)}")
    return


def solution(n):
    count = 0
    for i in range(2, n+1):
        isOk = True
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0: # 소수가 아니다.
                isOk = False
                break
        if isOk:
            count += 1
            print(i)

    return count


if __name__ == "__main__":
    mianJob(10)
    mianJob(5)