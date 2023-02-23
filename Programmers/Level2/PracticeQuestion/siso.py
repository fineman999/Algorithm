from collections import defaultdict
import itertools


def valid_twin(weight1, weight2):
    distance = [2, 3, 4]
    for i in range(3):
        for j in range(3):
            if weight1 * distance[i] == weight2 * distance[j]:
                # print(weight1, weight2)
                return True
    return False


def change_twin(weights, diary):
    distance = [2, 3, 4]
    for i in range(len(weights)):
        for dist in distance:
            diary[dist * weights[i]].append(i)


def solution(weights):
    diary = defaultdict(list)

    change_twin(weights, diary)

    answer = set()
    for key, value in diary.items():
        if len(value) >= 2:

            for i in itertools.combinations(value, 2):
                answer.add(i)

    return len(answer)