import time


def mianJob(data):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(data)}")
    return


def solution(numbers):
    full_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0
    for x in full_numbers:
        if x not in numbers:
            answer = answer + x

    return answer


if __name__ == "__main__":
    mianJob([1,2,3,4,6,7,8,0])
    mianJob([5,8,4,0,6,7,9])