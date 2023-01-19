from collections import deque

alpha = []
visited = []
def check_column(name, i):
    max_column = 99
    if name[i] != alpha[0]:
        for k in range(1, 25):
            if name[i] == alpha[k]:
                max_column = min(max_column, k)
                break
        k = -1
        while True:
            if name[i] == alpha[k]:
                max_column = min(max_column, abs(k))
                break
            k -= 1
    if max_column == 99:
        return 0
    return max_column


def final(i,name, result):
    if name[i] != 'A':
        result += check_column(name, i)
        name[i] = 'A'
    if name.count('A') != len(name):
        # print(name)
        # 제일 멀리있는 A가 아닌 값 찾기
        (result_right_cnt,right_i, right_cnt) = row(i+1, name)
        (result_left_cnt, left_i, left_cnt) = row_left(i-1, name)
        # print("right_cnt",right_cnt)
        # print("left_cnt", left_cnt)
        # 같을 경우 제일 가까이 있는 A가 아닌 값 찾기
        if right_cnt == left_cnt:
            (result_right_cnt, right_i, right_cnt) = row_2(i + 1, name)
            (result_left_cnt, left_i, left_cnt) = row_left_2(i - 1, name)
        if right_cnt < left_cnt:
            result += result_right_cnt
            result = final(right_i,name, result)
        else:
            result += result_left_cnt
            result = final(left_i,name, result)
    return result

def row_left(i, name):
    cnt = 1
    valid = False
    result_cnt = 0
    result_i = i
    compare_cnt = 0
    while cnt < len(name)//2+1 and abs(i) < len(name):
        if name[i] != 'A':
            compare_cnt = cnt
            if not valid:
                result_cnt = cnt
                result_i = i
                valid = True
        cnt += 1
        i -= 1
    if compare_cnt == 0:
        compare_cnt = 21
    return result_cnt, result_i, compare_cnt


def row_left_2(i, name):
    cnt = 1
    result_cnt = 0
    result_i = i
    compare_cnt = 0
    while abs(i) < len(name):
        if name[i] != 'A':
            compare_cnt = cnt
            result_cnt = cnt
            result_i = i
            break
        cnt += 1
        i -= 1
    if compare_cnt == 0:
        compare_cnt = 21
    return result_cnt, result_i, compare_cnt


def row_2(i, name):
    cnt = 1
    result_cnt = 0
    result_i = i
    compare_cnt = 0
    while abs(i) < len(name):
        if name[i] != 'A':
            compare_cnt = cnt
            result_cnt = cnt
            result_i = i
            break
        cnt += 1
        i += 1
    if compare_cnt == 0:
        compare_cnt = 21
    return result_cnt, result_i, compare_cnt


def row(i, name):
    cnt = 1
    valid = False
    result_cnt = 0
    result_i = i
    compare_cnt = 0
    while cnt < len(name)//2+1 and abs(i) < len(name):
        if name[i] != 'A':
            compare_cnt = cnt
            if not valid:
                result_cnt = cnt
                result_i = i
                valid = True
        cnt += 1
        i += 1
    if compare_cnt == 0:
        compare_cnt = 21
    return result_cnt, result_i, compare_cnt




def solution(name):
    global alpha
    global visited
    alpha = [chr(i) for i in range(65,91)]
    visited = [False]*len(name)
    name = list(name)

    start = 0
    answer = final(start,name,0)

    return answer




def main():

    return print(solution("JAN"))


if __name__ == "__main__":
    main()
