import time


def mianJob(s):
    start = time.time()
    print(solution(s))
    print(f"[time]\t{time.time()-start:.5f}")
    return


def solution(s):

    # 길이 체크
    if not (len(s)==4 or len(s) ==6):
        return False

    # 숫자구성인지 체크
    try:
        s = int(s)
    except Exception as e:
        return False
    return True


if __name__ == "__main__":
    mianJob("a234")
    mianJob("1234")
    mianJob("123456")
    mianJob("12345")
    mianJob("1s2345")