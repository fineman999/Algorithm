from collections import deque
def check_right(u):
    queue = deque(u)
    stack = deque()
    while queue:
        queue_pop = queue.popleft()
        if not stack:
            stack.append(queue_pop)
        else:
            stack_pop = stack.pop()
            if stack_pop == "(" and queue_pop == ")":
                continue
            stack.append(stack_pop)
            stack.append(queue_pop)
    if stack:
        return False
    return True


def change(u):
    change_u = ""
    for i in range(len(u)):
        if u[i] == '(':
            change_u += ")"
        else:
            change_u += "("
    return change_u


def solution(p):
    answer = ''
    # 1

    u_final = ""
    v_final = ""
    while True:
        if p == "":
            return u_final+p
        u_left = 0
        u_right = 0
        u = ""
        v = ""
        # 2
        for i in range(len(p)):
            if p[i] == "(":
                u_left += 1
            else:
                u_right += 1
            if u_right == u_left:
                u = p[:i+1]
                v = p[i+1:]
                break
        # 3
        valid = check_right(u)
        if valid:
            if check_right(v):
                return u_final + p
            u_final += u
            p = v
            continue
        # 4
        else:
            # 4-1,4-2,4-3
            bean_str = "(" + v + ")"
            change_u = change(u[1:-1])
            answer = u_final + bean_str + change_u
            break
    return answer

def main():
    print(solution("(()())()"))


if __name__ == "__main__":
    main()
