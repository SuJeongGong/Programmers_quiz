import time


def mianJob(s):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(s)}")
    return


def solution(s):
    lower = [c for c in s if c.islower()]
    upper = [c for c in s if not c.islower()]
    return "".join(sorted(lower, reverse=True)) + "".join(sorted(upper, reverse=True))


if __name__ == "__main__":
    mianJob("Zbcdefg")