import time


def mianJob(n):
    start = time.time()
    print(solution(n))
    print(f"[time]\t{time.time()-start:.5f}")
    return


def solution(n):
    number_3 = number_10 = []
    # 3진법으로 변환
    while(True):
        number_3.append(n % 3)
        n = n//3
        if(n<3):
            number_3.append(n)
            break

    number_3 = int(str(number_3)[1:-1].replace(',',"").replace(' ',""))
    # 10진법으로 변환
    while(True):
        number_10.append(number_3 % 10)
        number_3 = number_3 // 10

        if(number_3<10):
            number_10.append(number_3)
            break

    number_10 = int(str(number_10)[1:-1].replace(',',"").replace(' ',""))
    return number_10


if __name__ =="__main__":
    mianJob(45)
    mianJob(125)