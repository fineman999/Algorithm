import math
import sys
# 덧셈, 뺄셈, 곱셈, 나눗셈
max_answer = -math.inf
min_answer = math.inf
def dfs(sequence, operators, index, result, N):
    if index == N:
        global max_answer
        global min_answer
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
        return

    # 덧셈
    if operators[0] > 0:
        operators[0] -= 1
        dfs(sequence, operators, index + 1, result + sequence[index], N)
        operators[0] += 1
    if operators[1] > 0:
        operators[1] -= 1
        dfs(sequence, operators, index + 1, result - sequence[index], N)
        operators[1] += 1
    if operators[2] > 0:
        operators[2] -= 1
        dfs(sequence, operators, index + 1, result * sequence[index], N)
        operators[2] += 1
    if operators[3] > 0:
        operators[3] -= 1
        if result > 0:
            dfs(sequence, operators, index + 1, result//sequence[index], N)
        else:
            dfs(sequence, operators, index + 1, -(-result // sequence[index]), N)
        operators[3] += 1


def solution(N, sequence, operators):

    dfs(sequence,operators, 1, sequence[0], N)

    print(max_answer)
    print(min_answer)



def main():
    N = int(sys.stdin.readline())
    sequence = list(map(int, sys.stdin.readline().rstrip().split()))
    operators = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, sequence, operators)

if __name__ == '__main__':
    main()
