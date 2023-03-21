import copy
import sys
from collections import deque
import re
def recursive(str1):
    q = []
    stack = deque()
    for i in range(len(str1)):
        if str1[i].isalpha():
            q.append(str1[i])
        else:
            if str1[i] == '(':
                stack.append(str1[i])
            elif str1[i] == ')':
                while stack:
                    check = stack.pop()
                    if check == '(':
                        break
                    q.append(check)
            elif str1[i] == '*' or str1[i] == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    q.append(stack.pop())
                stack.append(str1[i])
            else:
                while stack and stack[-1] != '(':
                    q.append(stack.pop())
                stack.append(str1[i])
    while stack:
        q.append(stack.pop())
    return q

def solution(str1):

    print("".join(recursive(str1)))




def main():
    str1 = sys.stdin.readline().rstrip()
    solution(str1)


if __name__ == '__main__':
    main()