import time
import re

def mianJob(new_id):
    start = time.time()
    print(f"[time]\t{time.time() - start:.5f}\t [answer] : {solution(new_id)}")
    return


def solution(new_id):
    new_id_update = re.sub( "\.+", ".", re.sub("[^a-z0-9\.\_\-]", "", new_id.lower()))
    new_id_update = re.sub("(^\.|\.$)", "", new_id_update)
    if new_id_update == "":
        new_id_update = "a"
    if len(new_id_update) > 15:
        new_id_update = new_id_update[:15]
        new_id_update = re.sub("(^\.|\.$)", "", new_id_update)

    if len(new_id_update) < 3:
        new_id_update += new_id_update[-1] + new_id_update[-1] + new_id_update[-1]
        new_id_update = new_id_update[0:3]

    return new_id_update


if __name__ == "__main__":
    mianJob("...!@BaT#*..y.abcdefghijklm")
    mianJob("z-+.^.")
    mianJob("=.=")
    mianJob("123_.def")
    mianJob("abcdefghijklmn.p")
