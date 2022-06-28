import time


def mianJob(d, budget):
    start = time.time()
    print(f"[time]\t{time.time() - start:.5f}\t [answer] : {solution(d, budget)}")
    return


def solution(d, budget):
    if sum(d) == budget:
        return len(d)

    d = sorted(d)

    result = [0]
    for i1 in range(len(d)):
        for i2 in range(len(d)):
            if sum(d[i1:i2+1]) <= budget:
                result.append(len(d[i1:i2+1]))

    return max(result)


if __name__ == "__main__":
    mianJob([1,3,2,5,4],	9)
    mianJob([2,2,3,3],	10)