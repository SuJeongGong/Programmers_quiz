import time


def mianJob(data1 ,data2):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(data1, data2)}")
    return


def solution(numbers, divisor):
    answer = [n for n in numbers if n % divisor == 0]

    if len(answer) ==0:
        return [-1]
    else:
        return sorted(answer)


if __name__ == "__main__":
    mianJob([5, 9, 7, 10],	5)
    mianJob([2, 36, 1, 3],	1)
    mianJob([3,2,6],	10)