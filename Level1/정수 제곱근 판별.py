import time
import math

def mianJob(n):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(n)}")
    return


def solution(n):
    return (int(math.sqrt(n)) + 1) ** 2 if math.sqrt(n) % 1 == 0 else -1


if __name__ == "__main__":
    mianJob(121)
    mianJob(3)