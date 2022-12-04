def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if not stack:
            stack.append(s[i])
        else:
            stack_pop = stack.pop()
            if stack_pop != s[i]:
                stack.append(stack_pop)
                stack.append(s[i])
    if stack:
        return 0
    return 1



def main():
    print(solution("cdcd"))


if __name__ == "__main__":
    main()
