import time


def mianJob(strings, n):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(strings, n)}")
    return


def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x)) # n번째로 정렬, 중복인 경우에는 단어자체로 sort

    return strings


if __name__ == "__main__":
    mianJob(["sun", "bed", "car"],1)
    mianJob(["abce", "abcd", "cdx"],2)