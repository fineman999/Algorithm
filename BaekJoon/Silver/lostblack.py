import sys


def solution(arr):
    check = 1
    answer = 0
    for element in arr:
        if element.isdigit():
            answer += int(element)*check
        elif element == '-':
            check = -1
    return answer


def main():
    check = sys.stdin.readline().rstrip()
    arr = []
    number = ''
    for i in range(len(check)):
        if check[i].isdigit():
            number += check[i]
        else:
            arr.append(number)
            arr.append(check[i])
            number = ''
    if len(number) > 0:
        arr.append(number)
    print(solution(arr))


if __name__ == "__main__":
    main()