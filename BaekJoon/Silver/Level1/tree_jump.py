import sys


def solution(N, arr):
    arr.sort()
    visited = [0]*N
    cnt = 0
    for i in range(N):
        if i%2==0:
            visited[cnt] = arr[i]
            cnt += 1
        else:
            visited[-cnt] = arr[i]
    answer = abs(visited[0] - visited[-1])
    for i in range(N-1):
        answer = max(abs(visited[i] - visited[i+1]), answer)
    return answer


def main():
    T = int(sys.stdin.readline().rstrip())
    answer = []
    for _ in range(T):
        N = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().rstrip().split()))
        answer.append(solution(N, arr))
    for ele in answer:
        print(ele)
if __name__ == '__main__':
    main()