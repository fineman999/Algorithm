import itertools

def solution(orders, course):

    answer = []
    for element in course:
        dictionary = dict()
        for j in range(len(orders)):
            combinations = itertools.combinations(orders[j], element)
            for combination in combinations:
                sort_combination = list(combination)
                sort_combination.sort()
                combination = "".join(sort_combination)
                if combination not in dictionary:
                    dictionary[combination] = 0
                else:
                    dictionary[combination] +=1
        max_value = 0
        for key, value in dictionary.items():
            max_value = max(value, max_value)
        if max_value < 1:
            continue
        for key, value in dictionary.items():
            if max_value == value:
                answer.append(key)

    return sorted(answer)


def main():
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]	))


if __name__ == "__main__":
    main()
