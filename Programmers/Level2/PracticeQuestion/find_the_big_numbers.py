from collections import deque


def solution(numbers):
    stack = deque([numbers[-1]])
    n = len(numbers)
    answer = [-1] * n

    for i in range(n-2, -1, -1):
        if numbers[i] >= stack[0]:
            stack = deque([numbers[i]])
        else:
            while stack:
                if stack[-1] > numbers[i]:
                    answer[i] = stack[-1]
                    stack.append(numbers[i])
                    break
                stack.pop()
    return answer


def main():
    print(solution([9, 1, 5, 3, 6, 2]))


if __name__ == "__main__":
    main()