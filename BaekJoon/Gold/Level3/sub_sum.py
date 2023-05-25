import sys


def solution(N, M, arr):

    reminder = [0]*(M+1)
    total = 0
    for i in range(N):
        total += arr[i]
        r = total%M
        reminder[r] += 1
    reminder[0] += 1

    count = 0
    for i in reminder:
        count += i*(i-1)//2

    print(count)


def main():
    N, M = inputs()
    arr = list(inputs())
    solution(N, M, arr)


def inputs():
    return map(int, sys.stdin.readline().rstrip().split())

if __name__ == '__main__':
    main()