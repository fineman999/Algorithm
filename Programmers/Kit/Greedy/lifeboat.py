from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)
    answer = 0
    while people:
        people_popleft = people.popleft()
        if people and people_popleft + people[-1] <= limit:
            people.pop()
        answer += 1

    return answer


def main():
    print(solution(	[70, 50, 80, 50], 100))


if __name__ == "__main__":
    main()