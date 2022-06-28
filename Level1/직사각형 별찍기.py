import time


def mianJob(a, b ):
    start = time.time()
    print(f"[time]\t{time.time() - start:.5f}\t [answer] : {solution(a, b )}")
    return


def solution(a, b):
    for i in range(b):
        print("*" * a)
    return


if __name__ == "__main__":
    mianJob(5, 3)
