from collections import deque

def solution(arr):
    arr = deque(arr)
    stack = deque()
    stack.append(arr.popleft())
    while arr:
        popleft = arr.popleft()
        if stack[-1] != popleft:
            stack.append(popleft)

    return list(stack)

def main():
    print(solution(	[1, 1, 3, 3, 0, 1, 1]))

if __name__ == "__main__":
    main()
