from collections import deque
def compare(stack_pop, queue_pop):
    if stack_pop == "(" and queue_pop == ")":
        return 0
    elif stack_pop == "{" and queue_pop == "}":
        return 0
    elif stack_pop == "[" and queue_pop == "]":
        return 0
    elif queue_pop == "(" or queue_pop == "{" or queue_pop == "[":
        return 1
    else:
        return 2



def solution(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        queue = deque(s[i:]+s[:i])
        stack = deque()
        valid = True
        while queue:
            queue_popleft = queue.popleft()
            if not stack:
                stack.append(queue_popleft)
            else:
                stack_pop = stack.pop()
                if stack_pop == "]" or stack_pop == ")" or stack_pop == "}":
                    valid = False
                    break
                if compare(stack_pop, queue_popleft) == 1:
                    stack.append(stack_pop)
                    stack.append(queue_popleft)
                elif compare(stack_pop, queue_popleft) == 2:
                    valid = False
                    break
        if valid and not stack:
            cnt += 1
    return cnt

def main():
    print(solution("[](){}"))


if __name__ == "__main__":
    main()
