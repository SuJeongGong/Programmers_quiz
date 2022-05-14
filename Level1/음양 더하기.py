import time


def mianJob(absolutes ,signs):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(absolutes ,signs)}")
    return


def solution(absolutes ,signs):
    answer = 0
    for i, x in enumerate(absolutes):
        answer += x if signs[i] else -x
    return  answer


if __name__ == "__main__":
    mianJob([4,7,12], [True,False,True])
    mianJob([1,2,3], [False,False,True])