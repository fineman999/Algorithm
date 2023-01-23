from collections import deque

def solution(k, score):
    queue = []
    answer = []
    for element in score:
        queue.append(element)
        if len(queue) == k + 1:
            queue.remove(min(queue))
        answer.append(min(queue))
    return answer


def main():
    print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))


if __name__ == "__main__":
    main()