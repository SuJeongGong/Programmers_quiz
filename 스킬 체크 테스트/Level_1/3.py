import time


def mianJob(password, n):
    start = time.time()
    print(solution(password, n))
    print(f"[time]\t{time.time()-start:.5f}")
    return


def solution(password, n):
    new_password = ""
    for index, x in enumerate(password):
        if x != " ":
            if((ord(x)+n)>90 or (ord(x)+n) > 122):
                new_password = new_password + chr(ord(x)+n-26)
            else:
                new_password = new_password + chr(ord(x)+n)
        else:
            new_password = new_password + " "

    return new_password


if __name__ == "__main__":
    mianJob("AB",1)
    mianJob("z",1)
    mianJob("a B z",4)