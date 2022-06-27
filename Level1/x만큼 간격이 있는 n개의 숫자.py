import time


def mianJob(num):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(num)}")
    return


def collatz(n):
    if n%2==0:
        return n / 2
    else:
        return n * 3 + 1

def solution(num):
    cnt = 0
    while num != 1 and  num != 0:
        num = collatz(num)
        cnt = cnt +1
        if cnt > 500:
            cnt = -1
            break
    return cnt


if __name__ == "__main__":
    mianJob(6)
    mianJob(16)
    mianJob(626331)