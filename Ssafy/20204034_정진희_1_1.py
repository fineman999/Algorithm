import sys


def solution(arr):
    check = set()
    for i in range(len(arr)):
        if arr[i] not in check:
            if i + 1 < len(arr) and arr[i] != arr[i + 1]:
                check.add(arr[i])
        else:
            return False
    return True


def main():
    n = int(sys.stdin.readline().rstrip())
    answer = 0
    for _ in range(n):
        arr = sys.stdin.readline().rstrip()
        if solution(arr):
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()
