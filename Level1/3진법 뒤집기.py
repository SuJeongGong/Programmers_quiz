import time


def mianJob(input_num):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(input_num)}")
    return


def solution(n):
    number_3 = ""   # 3진법
    number_10 = 0   # 10진법

    while n >= 3:
        number_3 = str(n % 3) + number_3
        n = n // 3
    number_3 = str(n) + number_3
    number_3 = str(int("".join(reversed(list(number_3)))))

    for i, x in enumerate(number_3):
        number_10 = number_10 + int(int(x) * (3 ** (len(number_3) - 1 - i)))

    return number_10


if __name__ == "__main__":
    mianJob(3)
    # mianJob("2three45sixseven")
    # mianJob("123")
    # mianJob("one")