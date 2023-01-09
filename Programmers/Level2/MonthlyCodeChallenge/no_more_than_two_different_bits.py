def recursive(number):
    if number <= 1:
        return str(number)
    divide = number//2
    remain = number%2
    return recursive(divide) + str(remain)

# def solution(numbers):
#
#     answer = []
#     visited = dict()
#     for number in numbers:
#         if number not in visited:
#             visited[number] = recursive(number)
#
#         cnt = number + 1
#         while True:
#             if cnt not in visited:
#                 visited[cnt] = recursive(cnt)
#
#             if len(visited[number]) != len(visited[cnt]):
#                 visited[number] = "0"*(len(visited[cnt]) - len(visited[number]))+visited[number]
#
#             circulate = bin(bin(int("0b"+visited[number])) ^ bin(int("0b"+visited[cnt])))
#
#             if circulate <= 2:
#                 answer.append(cnt)
#                 break
#             else:
#                 cnt += 1
#
#
#     return answer
def solution(numbers):

    answer = []
    for number in numbers:
        check_number = recursive(number)
        # if "0" not in check_number:
        #     answer.append(number + (2 ** (check_number.count("1") - 1)))
        if check_number[-1] == "0":
            answer.append(number + 1)
        else:
            cnt = 0
            for j in range(len(check_number)-1,-1,-1):
                if check_number[j] == "0":
                    break
                cnt += 1
            answer.append(number + (2 ** (cnt - 1)))
    return answer


def main():
    print(solution([2, 9]))


if __name__ == "__main__":
    main()