import time


def mianJob(answers):
    start = time.time()
    print(solution(answers))
    print(f"[time]\t{time.time()-start:.5f}")
    return


def solution(answers):
    user_count1 = user_count2 = user_count3 = 0
    user_answer1 = [1, 2, 3, 4, 5]  # 5개
    user_answer2 = [2, 1, 2, 3, 2, 4, 2, 5]
    user_answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    winner = []

    for index, answer in enumerate(answers):
        # 갯수 증가
        if user_answer1[index % len(user_answer1)] == answer:
            user_count1 = user_count1 + 1
        if user_answer2[index % len(user_answer2)] == answer:
            user_count2 = user_count2 + 1
        if user_answer3[index % len(user_answer3)] == answer:
            user_count3 = user_count3 + 1

    # 어떤사람이 가장 높은지 비교
    winner_count = max([user_count1, user_count2, user_count3])
    if user_count1 == winner_count:
        winner.append(1)
    if user_count2 == winner_count:
        winner.append(2)
    if user_count3 == winner_count:
        winner.append(3)

    return winner


if __name__ =="__main__":
    mianJob([1,2,3,4,5])
    mianJob([1,3,2,4,2])