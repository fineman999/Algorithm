def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += str(i) * (food[i]//2)
    answer_reverse = answer[::-1]
    answer += "0"+answer_reverse

    return answer


def main():
    print(solution([1, 3, 4, 6]))


if __name__ == "__main__":
    main()
