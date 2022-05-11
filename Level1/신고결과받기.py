import time


def mianJob(id_list, report, k):
    start = time.time()
    print(solution(id_list, report, k))
    print(f"[time]\t{time.time()-start:.5f}")
    return


def solution(id_list, report, k):
    count_user = [0 for i in range(len(id_list))]

    # 유저별 신고 횟수 구하기
    for index, value in enumerate(set(report)):
        bad_user = value.split(" ")[1]
        user = value.split(" ")[0]
        count_user[id_list.index(bad_user)] = count_user[id_list.index(bad_user)] + 1

    # k번 이상 신고당한 유저 찾기
    bad_users = []
    for index, value in enumerate(count_user):
        if count_user[index] >= k:
            bad_users.append(id_list[index])

    # 나쁜 유저(k번이상 신고당한 유저)를 신고한 유저
    answer = [0 for i in range(len(id_list))]  # 메일을 받은 횟수를 id_list에 맞춰서
    for index_bad_user, bad_user in enumerate(bad_users):
        for row in report:
            if bad_user == row.split(" ")[1]:
                good_user_index = id_list.index(row.split(" ")[0])
                answer[good_user_index] = answer[good_user_index] + 1  # 신고한 유저

    return answer


if __name__ =="__main__":
    mianJob(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2
    )
    mianJob(	["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 2)