import time


def mianJob(n):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(n)}")
    return


def solution(n):
    return int("".join(sorted(str(n))[::-1]))


if __name__ == "__main__":
    mianJob(12)
    mianJob(118372)