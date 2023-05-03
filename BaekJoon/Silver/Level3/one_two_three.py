import sys

arr = [1,2,3]

def dfs(n, cnt):
    if cnt == n:
        return 1
    answer = 0
    for i in range(3):
        if cnt + arr[i] <= n:
            answer += dfs(n, cnt + arr[i])
    return answer



def solution(n):
    answer = dfs(n, 0)
    print(answer)


def main():
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        n = int(sys.stdin.readline().rstrip())
        solution(n)

if __name__ == '__main__':
    main()