def solution(answers):
    people = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    correct = [0, 0, 0]
    for i in range(len(answers)):
        for j in range(3):
            check = i % len(people[j])
            if people[j][check] == answers[i]:
                correct[j] += 1

    answer = []
    for index, score in enumerate(correct):
        if max(correct) == score:
            answer.append(index+1)
    return answer


def main():
    print(solution(	[1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
