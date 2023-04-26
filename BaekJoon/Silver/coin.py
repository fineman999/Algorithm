import sys


def solution(K, arr):
    answer = 0
    for i in range(len(arr)-1, -1, -1):
        if K >= arr[i]:
            temp = K//arr[i]
            K -= arr[i]*temp
            answer += temp
    print(answer)



def main():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for _ in range(N):
        arr.append(int(sys.stdin.readline().rstrip()))
    solution(K, arr)


if __name__ == '__main__':
    main()