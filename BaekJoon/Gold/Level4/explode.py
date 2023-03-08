import sys
from collections import deque

def solution(basic, explode):
    stack = []
    n = len(explode)
    i = 0
    while i < len(basic):

        stack.append(basic[i])

        if "".join(stack[-n:]) == explode:
            for _ in range(n):
                stack.pop()
        i += 1
    # print(stack)

    answer = "".join(list(stack))
    if answer == '':
        return "FRULA"
    return answer



def main():
    basic = sys.stdin.readline().rstrip()
    explode = sys.stdin.readline().rstrip()
    print(solution(basic, explode))

if __name__ == '__main__':
    main()
