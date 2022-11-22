def makeNumber(n, m) :
    '''
    1 ~ m 까지의 수를 더하여 n을 만드는 경우의 수를 1,000,000,007로 나눈 나머지를 반환하는 함수를 작성하세요.
    f(n) = f(n-1)+f(n-2)+...+f(n-m)
    '''

    memorize = [1]

    for i in range(1,n+1):
        sum_arr = 0
        for j in range(1,min(m,i)+1):
            sum_arr += memorize[i - j]
        memorize.append(sum_arr)

    return memorize[n]




def main():

    n, m = map(int, input().split())

    print(makeNumber(n, m))



if __name__ == "__main__":
    main()

