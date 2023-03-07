import sys
from collections import defaultdict
# parents = []
# def find_parents(number):
#     while number != parents[number]:
#         number = parents[number]
#     return number


def find_parents_using_dict(number, diary):
    start = number
    while number != diary[number]:
        number = diary[number]
    # 최적화 하기!!
    diary[start] = number
    return number


def solution(n, m, arr):
    diary = defaultdict(int)
    answer = []
    for types, a, b in arr:
        if diary.get(a) is None:
            diary[a] = a
        if diary.get(b) is None:
            diary[b] = b
        if types == 0:
            if a > b:
                a, b = b, a
            diary[find_parents_using_dict(b,diary)] = find_parents_using_dict(a, diary)
        elif types == 1:
            if find_parents_using_dict(a, diary) != find_parents_using_dict(b, diary):
                answer.append("NO")
            else:
                answer.append("YES")
    return answer

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())

    arr = []
    for i in range(m):
        arr.append(list(map(int, sys.stdin.readline().split())))
    answer = solution(n, m, arr)
    for ele in answer:
        print(ele)


if __name__ == "__main__":
    main()