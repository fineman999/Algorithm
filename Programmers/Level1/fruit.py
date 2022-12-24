from collections import deque
def solution(k, m, score):
    score.sort(reverse=True)
    score = deque(score)

    i = 0
    answer = []
    result = 0
    while score:
        if i == m:

            i = 0
            result += min(answer) * len(answer)
            answer = []

        else:
            answer.append(score.popleft())
            i += 1
    if len(answer) == m:
        result += min(answer) * len(answer)

    return result


def main():
    print(solution(4, 4, [4, 4, 3, 3, 3, 2, 2, 2, 1]))


if __name__ == "__main__":
    main()
