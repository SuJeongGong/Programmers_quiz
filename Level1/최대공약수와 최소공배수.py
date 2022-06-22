import time


def mianJob(n,m):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(n,m)}")
    return


def solution(n,m):
    answer = [-1, -1]
    for x in range(1, n+1)[::-1]:
        if n % x == 0 and m % x == 0:
            answer[0] = x
            break

    for x in range(m, n*m+1):
        if x % n == 0 and x % m == 0:
            answer[1] = x
            break

    return answer


if __name__ == "__main__":
    mianJob(3, 12)
    mianJob(2, 5)