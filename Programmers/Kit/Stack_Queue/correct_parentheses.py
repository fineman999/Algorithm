from collections import deque


def solution(s):
    s = deque(s)
    stack = deque()
    while s:
        s_popleft = s.popleft()
        if not stack:
            stack.append(s_popleft)
        else:
            if stack[-1] == "(" and s_popleft == ")":
                stack.pop()
                continue
            elif stack[-1] == "(" and s_popleft == "(":
                stack.append(s_popleft)
            else:
                return False
    if stack:
        return False
    return True

def main():
    print(solution("(())()"))

if __name__ == "__main__":
    main()
