import time


def mianJob(data1, data2, data3):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(data1, data2, data3)}")
    return


def solution(price, money, count):
    sum = 0
    for x in range(1, count+1):
        sum += price * x

    if money >= sum:
        return 0
    else:
        return sum - money


if __name__ == "__main__":
    mianJob(3,20,4)