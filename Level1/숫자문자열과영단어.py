import time
import re


def mianJob(s):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(s)}")
    return


def solution(s):
    NUMBER = {
        'zero': "0",
        "one": '1',
        "two": '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    findEnglish = re.compile("[a-zA-Z]+")

    answer = s
    for x in NUMBER.keys():
        if x in answer:
            # answer = answer.split(x)[0] + NUMBER[x] + answer.split(x)[1]
            answer = str(answer.split(x)).replace("['", "").replace("']", "").replace(" ", "").replace("','", NUMBER[x])
        if not findEnglish.search(answer):
            break

    return int(answer)


if __name__ == "__main__":
    mianJob("one4seveneighteight")
    mianJob("2four3four5six7")
    # mianJob("2three45sixseven")
    # mianJob("123")
    # mianJob("one")