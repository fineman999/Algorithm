import sys
import math
def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''

    max_result = 0

    for start in range(len(data)):
        for end in range(start, len(data)):
            result = 0
            for i in range(start, end):
                result += data[i]
                max_result = max(result, max_result)

    return max_result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
