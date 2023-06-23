import sys


def solution(arr):
    arr.sort(key=lambda x: (len(x), x))
    for i in range(len(arr)):
        print(arr[i])


def main():
    N = int(sys.stdin.readline().rstrip())
    arr = set()
    for _ in range(N):
        arr.add(sys.stdin.readline().rstrip())
    arr = list(arr)
    solution(arr)


if __name__ == '__main__':
    main()
