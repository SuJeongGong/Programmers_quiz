import time


def mianJob(numbers):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(numbers)}")
    return


def solution(numbers):
    answer =[]
    temp = -1
    for i in numbers:
        if i != temp:
            answer.append(i)
        temp = i
    return answer


if __name__ == "__main__":
    mianJob([1,1,3,3,0,1,1])
    mianJob([4,4,4,3,3])