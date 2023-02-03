

scores = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
personality = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
pointers = [['R','T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]


def solution(survey, choices):

    for i in range(len(survey)):
        [type_a, type_b] = list(survey[i])
        choice = choices[i]
        if choice == 4:
            continue
        elif choice > 4:
            personality[type_b] += scores[choice]
        else:
            personality[type_a] += scores[choice]

    answer = ''
    for type_a, type_b in pointers:
        if personality[type_b] > personality[type_a]:
            answer += type_b
        else:
            answer += type_a

    return answer


def main():
    print(solution(	["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))


if __name__ == "__main__":
    main()