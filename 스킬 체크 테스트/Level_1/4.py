import time


def mianJob(s):
    start = time.time()
    print(solution(s))
    print(f"[time]\t{time.time()-start:.5f}")
    return


def solution(s):
    answer =""
    for x in s.split(' '):
        # 각 단어마다
        for i, y in enumerate(x):
            # 짝수번째 -> 대문자
            if i%2 ==0:
                answer= answer + y.upper()
            # 홀수번째 -> 소문자
            else:
                answer = answer + y.lower()
        answer = answer + " "
    return answer[:-1]


if __name__ == "__main__":
    mianJob("try hello world")