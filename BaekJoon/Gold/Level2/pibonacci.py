import sys

REMINDER = 1_000_000_007
def matrix_multi(n, A, B):
    result =  [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= REMINDER
    return result

def matrix_pow(A, B):
    if B == 1:
        return A
    elif B == 2:
        return matrix_multi(2, A, A)
    else:
        temp = matrix_pow(A, B//2)
        if B % 2 == 0:
            return matrix_multi(2, temp, temp)
        else:
            return matrix_multi(2, matrix_multi(2, temp, temp), A)

def solution(n):
    A = [[1,1], [1,0]]

    answer = matrix_pow(A,n)
    print(answer[0][1] % REMINDER)

def main():
    n = int(sys.stdin.readline().rstrip())
    solution(n)

if __name__ == '__main__':
    main()