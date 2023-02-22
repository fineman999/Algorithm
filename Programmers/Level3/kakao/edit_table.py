from collections import deque, defaultdict


def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    diary = defaultdict(list)
    for i in range(n):
        if i == 0:
            diary[i] = [None, i+1]
        elif i == n-1:
            diary[i] = [i - 1, None]
        else:
            diary[i] = [i-1, i+1]

    stack = deque()
    for element in cmd:

        check = element.split()
        if len(check) == 2:
            [direct, index] = check
            index = int(index)
            if direct == "U":
                while index > 0:
                    k = diary[k][0]
                    index -= 1
            else:
                while index > 0:
                    k = diary[k][1]
                    index -= 1
        if check[0] == "C":
            if diary[k][0] is None:
                diary[diary[k][1]][0] = diary[k][0]
                stack.append(k)
                k = diary[k][1]
            elif diary[k][1] is None:
                diary[diary[k][0]][1] = diary[k][1]
                stack.append(k)
                k = diary[k][0]
            else:
                diary[diary[k][0]][1] = diary[k][1]
                diary[diary[k][1]][0] = diary[k][0]
                stack.append(k)
                k = diary[k][1]

        elif check[0] == "Z":
            check_k = stack.pop()
            if diary[check_k][0] is None:
                diary[diary[check_k][1]][0] = check_k
            elif diary[check_k][1] is None:
                diary[diary[check_k][0]][1] = check_k
            else:
                diary[diary[check_k][1]][0] = check_k
                diary[diary[check_k][0]][1] = check_k

    while stack:
        answer[stack.pop()] = "X"
    return "".join(answer)


def main():
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))


if __name__ == "__main__":
    main()