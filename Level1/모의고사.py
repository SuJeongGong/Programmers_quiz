import time

def mianJob(answers):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(answers)}")
    return


def solution(answers):

    check = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    result =[0,0,0]

    for i in range(len(answers)):
        if check[0][i % 5] == answers[i]:
            result[0] += 1
        if check[1][i % 8] == answers[i]:
            result[1] += 1
        if check[2][i % 10] == answers[i]:
            result[2] += 1

    return sorted([i + 1  for i, v in enumerate(result) if v == max(result)])


if __name__ == "__main__":
    mianJob([1,2,3,4,5])
    mianJob([1,3,2,4,2])