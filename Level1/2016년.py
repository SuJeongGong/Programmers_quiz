def mianJob(data1,data2):
    print(f"[answer] : {solution(data1, data2)}")
    return


def solution(a, b):
    import calendar
    week = {
        6: "SUN",
        0: "MON",
        1: "TUE",
        2: "WED",
        3: "THU",
        4: "FRI",
        5: "SAT"
    }
    return week[calendar.weekday(2016, a, b)]


if __name__ == "__main__":
    mianJob(5,24)
