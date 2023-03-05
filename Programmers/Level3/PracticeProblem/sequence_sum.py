
def solution(sequence):
    start_minus = []
    start_plus = []
    check = [1,-1]
    for i in range(len(sequence)):
        start_plus.append(sequence[i]*check[i%2])
        start_minus.append(sequence[i]*check[i%2]*-1)

    max_plus = [start_plus[0]]
    max_minus = [start_minus[0]]
    # print(start_plus)
    for i in range(1, len(sequence)):
        max_plus.append(max(start_plus[i], max_plus[-1] + start_plus[i]))
        max_minus.append(max(start_minus[i], max_minus[-1] + start_minus[i]))
    # print(max_plus, max_minus)
    answer = 0

    return max(max(max_plus), max(max_minus))


def main():
    print(solution([2,3,-6,1,3,-1,2,4]))



if __name__ == "__main__":
    main()