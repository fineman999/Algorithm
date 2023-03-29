import sys


def solution(S, problem):

    # for problem in problems:
    # 원소 추가
    if problem[0] == 'add':
        S |= (1 << int(problem[1]))
    # 원소 삭제
    elif problem[0] == 'remove':
        S = S & ~(1 << int(problem[1]))
    # 원소 확인
    elif problem[0] == 'check':
        print(1 if S & (1 << int(problem[1])) != 0 else 0)
    ## 있으면 추가, 없으면 삭제
    elif problem[0] == 'toggle':
        S = S ^ (1 << int(problem[1]))
    elif problem[0] == 'all':
        S = (1 << 21) - 1
    else:
        S = 0
    return S



def main():
    M = int(sys.stdin.readline().rstrip())
    problems = []
    S = 0
    for _ in range(M):
        S = solution(S, list(sys.stdin.readline().rstrip().split()))
        # problems.append(list(sys.stdin.readline().rstrip().split()))

    # solution(M, problems)


if __name__ == '__main__':
    main()