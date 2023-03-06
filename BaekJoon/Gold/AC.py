
from collections import deque
import sys


def solution(p, n, arr):
    if arr[0] == '':
        arr = deque()
    else:
        arr = deque(arr)
    check = 1
    for i in range(len(p)):
        if p[i] == 'R':
            check = check*-1
        else:
            if len(arr) < 1:
                return 'error'
            else:
                if check == 1:
                    arr.popleft()
                else:
                    arr.pop()
    arr = list(arr)
    if check == 1:
        return f'[{",".join(arr)}]'

    return f'[{",".join(arr[::-1])}]'


def main():
    T = int(sys.stdin.readline())
    answer = []
    for i in range(T):
        p = list(sys.stdin.readline().split()[0])
        n = int(sys.stdin.readline())

        check = sys.stdin.readline().split()[0]
        check_2 = check.split('[')[1]
        check_3 = check_2.split(']')[0]
        check_4 = list(check_3.split(','))
        arr = check_4
        answer.append(solution(p, n, arr))

    for ele in answer:
        print(ele)

if __name__ == "__main__":
    main()