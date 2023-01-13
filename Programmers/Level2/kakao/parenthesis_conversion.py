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

def numberOne(p):

    u_left = 0
    u_right = 0
    u = ""
    v = ""
    for i in range(len(p)):
        if p[i] == "(":
            u_left += 1
        else:
            u_right += 1
        if u_right == u_left:
            u = p[:i + 1]
            v = p[i + 1:]
            break
    return u, v
def recursive(p):
    # 1
    if p == "":
        return p
    # 2
    (u,v) = numberOne(p)

    # 3
    if check_right(u):
        return u + recursive(v)
    # 4
        # 4-1,4-2,4-3
    bean_str = "(" + recursive(v) + ")"
    change_u = change(u[1:-1])
    return bean_str + change_u

def solution(p):
    return recursive(p)

def main():
    print(solution("(()())()"))


if __name__ == "__main__":
    main()
