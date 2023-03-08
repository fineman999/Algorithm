import sys


def solution(N, arr):

    # arr = list(arr)
    arr.sort(key=lambda x:(x[1],x[0]))
    check = [0,0]
    answer = 0
    for i in arr:
        if check[1] <= i[0]:
            check = i
            answer += 1

    print(answer)


def main():
    N = int(sys.stdin.readline())
    arr = []
    for i in range(N):
        arr.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, arr)


if __name__ == '__main__':
    main()
