import time


def mianJob(s):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(s)}")
    return


def solution(s):
    import re
    find_p = re.compile("p|P")
    find_y = re.compile("y|Y")

    if len(find_p.findall(s)) == len(find_y.findall(s)):
        return True
    else:
        return False


if __name__ == "__main__":
    mianJob("pPoooyY")
    mianJob("Pyy")