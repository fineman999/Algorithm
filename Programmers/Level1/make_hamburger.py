from collections import deque


def solution(ingredient):
    queue = deque(ingredient)
    stack = deque()
    answer = 0
    while queue:
        popleft = queue.popleft()
        if popleft == 1 and stack and len(stack) > 2:
            valid = True
            for i in range(1, 4):
                if stack[-i] != 4-i:
                    valid = False
                    break
            if valid:
                for _ in range(3):
                    stack.pop()
                answer += 1
            else:
                stack.append(popleft)
        else:
            stack.append(popleft)

    return answer


def main():
    print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))


if __name__ == "__main__":
    main()