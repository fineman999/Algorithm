import sys
sys.setrecursionlimit(100000)

def convertBinary(n) :
    '''
    10진수 n을 2진수로 변환하여 반환합니다.

    *주의* : 변환된 2진수는 문자열이어야 합니다.

    예를 들어, 19가 입력될 경우 문자열 "10011"이 반환되어야 합니다.
    '''

    result = []
    while True:
        if n == 1 or n == 0:
            result.append(str(n))
            break
        remainder = n % 2
        n = n//2
        result.append(str(remainder))

    return "".join(result[::-1])



def main():
    '''
    이 부분은 수정하지 마세요.
    '''


    n = int(input())

    print(convertBinary(n))

if __name__ == "__main__":
    main()
