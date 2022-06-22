import time


def mianJob(n):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(n)}")
    return


def solution(n):
    answer = 0
    for x in str(n):
        answer = answer + int(x)
    return answer


if __name__ == "__main__":
    mianJob(123)
    mianJob(987)