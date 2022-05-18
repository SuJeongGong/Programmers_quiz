import time


def mianJob(numbers):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(numbers)}")
    return


def solution(numbers):
    return int(numbers)


if __name__ == "__main__":
    mianJob("1234")
    mianJob("-123")