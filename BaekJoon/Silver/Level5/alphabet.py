import sys

diary = {
    'c=',
    "c-",
    "dz=",
    "d-",
    "lj",
    "nj",
    "s=",
    "z="
}


def solution(arr):
    temp = ''
    answer = 0

    right = 0
    left = 0
    while left < len(arr):
        while right < len(arr) and right - left < 4:
            temp += arr[right]
            if temp in diary:
                answer += 1
                right += 1
                left = right
                temp = ''
            else:
                right += 1
        if temp != "":
            left += 1
            answer += 1
            right = left
            temp = ""

    print(answer)


def main():
    n = sys.stdin.readline().rstrip()
    solution(n)


if __name__ == '__main__':
    main()
