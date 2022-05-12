import time


def mianJob(data1 ,data2):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(data1, data2)}")
    return


def solution(a, b):
    if a == b:
        return a
    else:
        if a > b:
            array = range(b, a+1)
        else:
            array = range(a, b+1)

        return sum([i for i in array])


if __name__ == "__main__":
    mianJob(3,	5)
    mianJob(3,	3)
    mianJob(5,	3)
