import sys


def solution(str1, str2):
    stack = []
    n = len(str2)
    for i in range(len(str1)):
        stack.append(str1[i])
        if str2[-1] == stack[-1]:
            if "".join(stack[-n:]) == str2:
                for _ in range(n):
                    stack.pop()
    if not stack:
        return "FRULA"
    return "".join(stack)


def main():
    str1 = sys.stdin.readline().rstrip()
    str2 = sys.stdin.readline().rstrip()
    print(solution(str1, str2))

if __name__ == '__main__':
    main()