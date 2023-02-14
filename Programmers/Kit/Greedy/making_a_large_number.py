from collections import deque

def solution(number, k):
    number = list(map(int, number))
    queue = deque(number)
    stack = deque()

    cnt = 0
    while queue:
        if cnt == k:
            break
        if not stack:
            stack.append(queue.popleft())
        elif stack[-1] < queue[0]:
            stack.pop()
            cnt += 1
        else:
            stack.append(queue.popleft())

    if cnt < k:
        while stack:
            if cnt == k:
                break
            stack.pop()
            cnt += 1

    return "".join(list(map(str, stack)) + list(map(str, queue)))


def main():
    print(solution("1231234", 7))


if __name__ == "__main__":
    main()