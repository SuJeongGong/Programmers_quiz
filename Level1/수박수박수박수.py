import time


def mianJob(n):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(n)}")
    return


def solution(n):
    # if n % 2 == 0:
    #     return "".join(["수박" for x in range(n//2)])
    # else:
    #     return "".join(["수박" for x in range(n//2)]) + "수"
    return "수박" * (n//2) + "수" * (n % 2)


if __name__ == "__main__":
    mianJob(3)
    mianJob(4)