import time


def mianJob(s):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(s)}")
    return


def solution(s):
    n = len(s)
    i = len(s) // 2
    if n % 2 == 0:
        return s[i-1:i+1]
    else:
        return s[i:i+1]


if __name__ == "__main__":
    mianJob("abcde")
    mianJob("qwer")
