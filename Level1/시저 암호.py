import time


def mianJob(s, n):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(s, n)}")
    return


def solution(s, n):
    # answer = ""
    # for x in s:
    #     if x == " ":
    #         answer += " "
    #     elif x.islower() and ord(x)+n >= 123:
    #         if ord(x)+n-26 >= 123:
    #             answer += chr(ord(x)+n-26-26)
    #         else:
    #             answer += chr(ord(x)+n-26)
    #     elif x.isupper() and ord(x)+n >= 91:
    #         if ord(x)+n-26 >= 91:
    #             answer += chr(ord(x)+n-26-26)
    #         else:
    #             answer += chr(ord(x)+n-26)
    #     else:
    #         answer += chr(ord(x) + n)
    # return answer

    return "".join([chr(ord(x)+n-26) if (x.islower() and ord(x)+n >= 123) or (x.isupper() and ord(x)+n >= 91) else x if x ==" " else chr(ord(x)+n) for x in s])


if __name__ == "__main__":
    # mianJob("AB", 1)
    # mianJob("z", 1)
    mianJob("a B z", 24)
    mianJob("a    b", 1)