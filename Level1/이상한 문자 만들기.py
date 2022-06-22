import time
import re


def mianJob(s):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(s)}")
    return


def solution(s):
    # answer = ""
    # for x in s.split(" "):
    #     for index, y in enumerate(x):
    #         if index % 2 == 0:
    #             answer = answer + y.upper()
    #         else:
    #             answer = answer + y.lower()
    #     answer = answer + " "
    # return answer[:-1]

    # return "".join([y.upper() if index % 2 == 0 else y.lower() for x in s.split(" ") for index, y in enumerate(x)])
    return " ".join(["".join(y.upper() if index % 2 == 0 else y.lower() for index, y in enumerate(x)) for x in s.split(" ")])


if __name__ == "__main__":
    mianJob("try hello world")