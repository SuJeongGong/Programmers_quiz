import time


def mianJob(phone_number):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(phone_number)}")
    return


def solution(phone_number):
    return "".join(["*" if x < (len(phone_number)-4) else phone_number[x] for x in range(len(phone_number))])


if __name__ == "__main__":
    mianJob("01033334444")
    mianJob("027778888")