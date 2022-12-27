import math

# def get_combinations(arr,n,s):
#     result = []
#     if n == 0:
#         if s == 0:
#             return [[]]
#         else:
#             return [[-1]]
#     for i in range(len(arr)):
#         ele = arr[i]
#         rest_arr = arr[i+1:]
#         for c in get_combinations(rest_arr, n-1, s-ele):
#             if -1 in c:
#                 continue
#             result.append([ele] + c)
#
#     return result


def solution(n, s):
    answer = s//n
    remain = n - s%n
    result = []
    if answer == 0:
        return [-1]
    for i in range(remain):
        result.append(answer)
    for i in range(n-remain):
        result.append(answer+1)
    return result




def main():
    print(solution(2, 9))


if __name__ == "__main__":
    main()
