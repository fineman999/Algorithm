import sys
def getNearestInternal(data, m):

    result = data[len(data) // 2]
    if result == m:
        return m

    if m < result:
        getNearestInternal(data[:m])
    else:
        getNearestInternal(data[m:])

def getNearest(data, m) :
    '''
    n개의 숫자가 list로 주어지고, 숫자 m이 주어질 때, n개의 숫자 중에서 m과 가장 가까운 숫자를 반환하는 함수를 작성하세요.
    '''


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(getNearest(data, m))

if __name__ == "__main__":
    main()
