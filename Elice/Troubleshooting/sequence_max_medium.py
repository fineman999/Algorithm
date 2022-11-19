import sys

def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''
    # 기저 조건
    if len(data) == 1:
        return data[0]

    medium = len(data) // 2


    left_max = getSubsum(data[:medium])
    right_max = getSubsum(data[medium:])
    sums = 0
    right_sum = 0
    left_sum = 0
    for i in range(medium - 1, -1, -1):
        sums += data[i]
        left_sum = max(sums, left_sum)
    sums = 0
    for i in range(medium, len(data), 1):
        sums += data[i]
        right_sum = max(sums, right_sum)

    return max([left_max, right_max, right_sum+left_sum])

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
