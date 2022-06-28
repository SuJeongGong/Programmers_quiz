import time


def mianJob(seoul):
    start = time.time()
    print(f"[time]\t{time.time() - start:.5f}\t [answer] : {solution(seoul)}")
    return


def solution(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다"


if __name__ == "__main__":
    mianJob(["Jane", "Kim"])