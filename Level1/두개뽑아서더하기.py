import time


def mianJob(data):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(data)}")
    return


def solution(numbers):
    answer = set()
    for ix, x in enumerate(numbers):
        for iy, y in enumerate(numbers):
            if ix != iy:
                answer.add(x + y)

    return sorted(list(answer))


if __name__ == "__main__":
    # mianJob([2,1,3,4,1])
    # mianJob([5,0,2,7])
    mianJob([1,0,1,0])
    mianJob([0,0,1,0])
    mianJob([2,13])