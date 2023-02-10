import math


def calculate(arr):
    result = 0
    min_element = [math.inf, math.inf]
    n = len(arr)
    check = [0]*len(arr)
    for i in range(n):
        [left_arr, right_arr] = min_element
        if arr[i] < left_arr:
            min_element[0] = arr[i]
            check[i] += 1
        if arr[n-1-i] < right_arr:
            min_element[1] = arr[n-i-1]
            check[n-i-1] += 1
    for i in check:
        if i > 0:
            result += 1
    return result


def solution(a):
    answer = calculate(a)
    return answer


def main():
    print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))


if __name__ == "__main__":
    main()
