import time

def mianJob(answers):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(answers)}")
    return


def solution(answers):

    check = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    # result = {1:0, 2:0, 3:0}
    result =[0,0,0]

    for i in range(len(answers)):
        if check[0][i % 5] == answers[i]:
            # result[1] += 1
            result[0] += 1
        if ((i+1) % 2 == 1 and answers[i] == 2) or ((i+1) % 2 == 0 and check[1][(i+1) // 2 % 4] == answers[i]):
            # result[0] += 1
            result[2] += 1
        if check[2][(i+1) % 10] == answers[i]:
            # result[3] += 1
            result[0] += 1

    return result.index(max(result))


if __name__ == "__main__":
    mianJob([1,2,3,4,5])
    mianJob([1,3,2,4,2])