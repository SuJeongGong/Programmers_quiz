import time


def mianJob(n):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(n)}")
    return


def solution(n):
     return "Even" if n % 2 == 0 else "Odd"


if __name__ == "__main__":
    mianJob(12)
    mianJob(5)