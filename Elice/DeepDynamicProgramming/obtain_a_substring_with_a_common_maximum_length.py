def LCS(s1, s2) :
    '''
    문자열 s1, s2의 최대 공통 부분 수열의 길이를 반환하는 함수를 작성하세요.
    '''
    m = len(s1)
    n = len(s2)

    L = [[None] * (n + 1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])



    print(L[m][n])

def main():

    s1 = input()
    s2 = input()

    return LCS(s1, s2)


if __name__ == "__main__":
    main()