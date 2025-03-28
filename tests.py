
def monobit_test(s, x):
    ones = 0
    for i in s:
        if i == x:
            ones += 1
    if ones > 9725 and ones < 10275:
        return True
    else:
        return False


def run_test(s, x):
    series = [0 for col in range(6)]
    series_ranges = [(2315, 2685), (114, 1386), (527, 723), (240, 384), (103,209), (103,209)]
    counter = 0
    for i in s:
        if i == x:
            counter += 1
        else:
            if counter > 5:
                series[5] += 1
            else:
                series[counter-1] +=1

            counter = 0

    for i in range(6):
        if series[i] < series_ranges[i][0] and series[i] > series_ranges[i][1]:
            return False

    return True


def long_run_test(s, x):
    counter = 0
    for i in s:
        if counter >= 26:
            return False
        if i == x:
            counter += 1
        else:
            counter = 0

    return True


def poker_test(s):
    test = 0
    arr = [0 for col in range(16)]
    index = 0
    while index < len(s):
        num = int(s[index]) * 8 + int(s[index + 1]) * 4 + int(s[index + 2]) * 2 + int(s[index + 3]) * 1
        arr[num] += 1
        index += 4
    for i in range(16):
        test += arr[i] * arr[i]
    test *= 16 / 5000
    test -= 5000
    if test > 2.16 and test < 46.17:
        return True
    else:
        return False
