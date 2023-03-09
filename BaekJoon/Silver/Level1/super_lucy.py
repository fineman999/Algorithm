import sys


def solution(N, arr):
    arr.sort()
    answer = [arr[0]]
    # print(arr)
    for i in range(1, len(arr)):
        [a,b] = arr[i]
        if answer[-1][1] > b:
            answer.append(arr[i])
    return len(answer)


def main():
    T = int(sys.stdin.readline())
    answer = []
    for _ in range(T):
        N = int(sys.stdin.readline())
        arr = []
        for i in range(N):
            arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
        answer.append(solution(N, arr))

    for ele in answer:
        print(ele)


if __name__ == '__main__':
    main()
