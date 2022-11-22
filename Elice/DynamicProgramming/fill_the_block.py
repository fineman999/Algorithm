def fillBox(n):
    '''
    2 x n 의 상자를 2 x 1 의 블럭으로 채우는 경우의 수를 1,000,000,007로 나눈 나머지를 반환하는 함수를 작성하세요.
    f(n) = f(n-1) + f(n+2)
    '''
    memorize = [1,1]

    for i in range(2,n+1):
        memorize.append(memorize[i-1] + memorize[i-2])

    return memorize[n]


def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    n = int(input())

    print(fillBox(n))


if __name__ == "__main__":
    main()
