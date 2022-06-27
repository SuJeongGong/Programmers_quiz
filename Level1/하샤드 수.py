import time


def mianJob(x):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(x)}")
    return


def solution(x):
     return True if x % sum([int(y) for y in str(x)]) == 0 else False


if __name__ == "__main__":
    mianJob(10)
    mianJob(12)
    mianJob(11)
    mianJob(13)