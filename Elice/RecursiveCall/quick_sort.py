def quickSort(array):
    '''
    퀵정렬을 통해 오름차순으로 정렬된 array를반환하는 함수를 작성하세요.
    '''
    if len(array) <=1:
        return array

    pivot = array[0]

    smaller = []
    bigger = []
    for ele in array[1:]:
        if pivot <= ele:
            bigger.append(ele)
        else:
            smaller.append(ele)
    return quickSort(smaller) + [pivot] + quickSort(bigger)


def getSmall(array, pivot):

    return None

def getBig(array, pivot):

    return None


def main():
    line = list(map(int, input().split()))

    print('정렬 결과:', *quickSort(line))


if __name__ == "__main__":
    main()
