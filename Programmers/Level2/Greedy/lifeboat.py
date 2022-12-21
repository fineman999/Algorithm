from collections import deque
def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)
    answer = 0

    while people:
        most_weight = people.popleft()
        try:

            little_weight = people.pop()
            weight = most_weight + little_weight
            answer += 1
            if weight > limit:
                people.append(little_weight)
        except:
            answer += 1

    return answer



def main():
    people = [70, 50, 80, 50]
    limit = 100
    print(solution(people, limit))


if __name__ == "__main__":
    main()
