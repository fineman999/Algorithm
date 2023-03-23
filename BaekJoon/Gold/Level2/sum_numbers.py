import sys
from collections import defaultdict

def solution(A, B, C, D, n):
    left = defaultdict(int)

    answer = 0
    for i in A:
        for j in B:
            left[i+j] += 1

    for i in C:
        for j in D:
            check = -(i+j)
            if check in left:
                answer += left[check]

    print(answer)


def main():
    A, B, C, D = [], [], [], []
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
    solution(A, B, C, D, n)

if __name__ == '__main__':
    main()