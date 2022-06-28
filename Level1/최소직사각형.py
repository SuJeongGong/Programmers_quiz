import time


def mianJob(sizes):
    start = time.time()
    print(f"[time]\t{time.time() - start:.5f}\t [answer] : {solution(sizes)}")
    return


def solution(sizes):
    return max([max(x) for x in sizes]) * max([min(x) for x in sizes])


if __name__ == "__main__":
    mianJob([[60, 50], [30, 70], [60, 30], [80, 40]])
    mianJob([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
    mianJob([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])