import time


def mianJob(n, arr1, arr2):
    start = time.time()
    print(f"[time]\t{time.time() - start:.5f}\t [answer] : {solution(n, arr1, arr2)}")
    return


def solution(n, arr1, arr2):
    result =[]
    for num1, num2 in zip(arr1, arr2):
        num1 = format(num1, 'b')
        while len(num1) < n:
            num1 = "0" + num1

        num2 = format(num2, 'b')
        while len(num2) < n:
            num2 = "0" + num2

        result.append("".join(["#" if x == '1' or y == '1' else " " for x, y in zip(num1, num2)]))

    return result


if __name__ == "__main__":
    mianJob(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
    mianJob(5, 	[46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])