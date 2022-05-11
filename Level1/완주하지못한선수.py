import time


def mianJob(participant, completion):
    start = time.time()
    print(solution(participant, completion))
    print(f"[time]\t{time.time()-start:.5f}")
    return


def solution(participant, completion):
    answer = ''
    participant = sorted(list(participant))
    completion = sorted(list(set(completion)))
    for x in completion:
        participant.remove(x)
    if len(participant) == 1:
        answer = participant[0]
    return answer


if __name__ =="__main__":
    # mianJob(["leo", "kiki", "eden"], ["eden", "kiki"])
    # mianJob(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
    mianJob(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])