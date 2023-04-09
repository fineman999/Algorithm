import sys
def matrix_multi(n, A,B):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def matrix_pow(N, A, B):
    # print(A)
    if B == 1:
        return A
    elif B == 2:
        return matrix_multi(N, A, A)
    else:
        temp = matrix_pow(N, A, B // 2)
        if B % 2 == 0:
            return matrix_multi(N, temp, temp)
        else:
            return matrix_multi(N, matrix_multi(N, temp, temp), A)

def solution(N, B, arr):
    # print(arr)
    temp = matrix_pow(N, arr, B)
    for ele in temp:
        for num in ele:
            print(num%1_000, end=' ')
        print()


def main():
    N, B = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, B, arr)


if __name__ == '__main__':
    main()