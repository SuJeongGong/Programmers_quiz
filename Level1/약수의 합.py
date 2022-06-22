import time


def mianJob(n):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(n)}")
    return


def solution(n):
    # answer = 0
    # for x in range(1, n+1):
    #     if n % x == 0:
    #         answer = answer + x
    # return answer

    return sum([x for x in range(1, n+1) if n % x == 0])


if __name__ == "__main__":
    mianJob(12)
    mianJob(5)