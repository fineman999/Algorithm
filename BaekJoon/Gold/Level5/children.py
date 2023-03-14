import sys


def solution(N, K, arr1):
    answer = []
    for i in range(N-1):
        answer.append(arr1[i+1]- arr1[i])
    answer.sort(reverse=True)

    return sum(answer[K-1:])




def main():
    N, K = map(int,sys.stdin.readline().rstrip().split())
    arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(N, K, arr1))

if __name__ == '__main__':
    main()