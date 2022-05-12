import time


def mianJob(data1, data2):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(data1, data2)}")
    return


def solution(left, right):
    answer = 0
    for x in range(left, right + 1):
        count = 0
        for y in range(1, x + 1):
            if x % y == 0:
                count += 1
        if count % 2 == 0:
            answer += x
        else:
            answer -= x

    return answer


if __name__ == "__main__":
    mianJob(13,17)
    mianJob(24,27)