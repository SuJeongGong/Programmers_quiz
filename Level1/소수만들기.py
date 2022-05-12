import time


def mianJob(data):
    start = time.time()
    print(f"[time]\t{time.time()-start:.5f}\t [answer] : {solution(data)}")
    return


def solution(numbers):
    count = 0
    answer = list()
    for ix, x in enumerate(numbers):
        for iy, y in enumerate(numbers[ix:]):
            for iz, z in enumerate(numbers[iy:]):
                if x != y and z != y and x != z:
                    temp_count = 0
                    for check in range(1, x + y + z + 1):
                        if (x + y + z) % check == 0:
                            temp_count += 1
                    if temp_count == 2 and sorted([x, y, z]) not in answer:
                        answer.append(sorted([x, y, z]))
                        count += 1

    return count


if __name__ == "__main__":
    mianJob([1,2,3,4])
    mianJob([1,2,7,6,4])