import time


def mianJob(s):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(s)}")
    return


def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    try:
        s = int(s)
        return True
    except Exception as e:
        return False


if __name__ == "__main__":
    mianJob("a234")
    mianJob("1234")