import collections
def solution(elements):

    n = len(elements)

    elements_sum = [element for element in elements]
    answer = set(elements_sum)

    elements = elements*n
    for i in range(1, n):
        for j in range(0, n):
            elements_sum[j] += elements[j+i]
        result = set(elements_sum)
        answer = answer | result

    return len(set(answer))



def main():
    print(solution([7,9,1,1,4]))


if __name__ == "__main__":
    main()