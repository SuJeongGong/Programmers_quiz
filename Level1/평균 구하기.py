import time


def mianJob(arr):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(arr)}")
    return


def solution(arr):
    return sum(arr) / len(arr)


if __name__ == "__main__":
    mianJob([1,2,3,4])
    mianJob([5,5])