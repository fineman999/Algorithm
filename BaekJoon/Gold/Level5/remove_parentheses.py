import sys

answer = set()
def dfs(str1):
    stack = []

    global answer
    for i in range(len(str1)):
        if str1[i] == '(':
            stack.append(i)
        elif str1[i] == ')':
            cnt = stack.pop()
            check = str1[cnt + 1:i]
            result = str1[:cnt] + check + str1[i + 1:]
            if result not in answer:
                answer.add(result)
                dfs(result)


def solution(str1):

    stack = []

    dfs(str1)

    result = list(answer)
    result.sort()
    for ele in result:
        print(ele)


def main():
    str1 = sys.stdin.readline().rstrip()
    solution(str1)

if __name__ == '__main__':
    main()