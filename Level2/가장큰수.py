import time
from itertools import *


def mianJob(numbers):
    start = time.process_time()
    result = solution(numbers)
    end = time.process_time()

    print(f"[time]\t{int(round((end - start) * 1000))}ms\t [answer] : {result}")
    return


def solution(numbers):
    # sum = []
    # for x in permutations([str(y) for y in numbers], len(numbers)):
    #     sum.append(int("".join(x)))
    #
    # return str(max(sum))
    # return "".join(sorted([str(x) for x in numbers], key=lambda x: (x[0]))[::-1])
    # return "".join(sorted([str(x) for x in numbers], key=lambda x: (-int(x[0]))))
    # return "".join(sorted([str(x) for x in numbers], key=lambda x:(x[y] for y in len(x)) if(len(x)>1) else x[0])[::-1])



if __name__ == "__main__":
    mianJob([6, 10, 2])
    mianJob([3, 30, 34, 5, 9])
    mianJob([3, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9, 30, 34, 5, 9])
