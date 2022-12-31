import itertools
from collections import deque


def operator(x,y,operation):
    if operation == '*':
        return x*y
    elif operation == "+":
        return x+y
    else:
        return x-y


def solution(expression):
    operation = set()
    numbers = []
    number = ""
    #1
    for i in range(len(expression)):
        if not expression[i].isdigit():
            numbers.append(number)
            number = ""
            numbers.append(expression[i])
            operation.add(expression[i])
        else:
            number += expression[i]

    permutations = itertools.permutations(operation, 3)
    result = 0
    for permutation in permutations:
        expression_no = numbers
        for per in permutation:
            j = 0
            while j < len(expression_no):
                if per == expression_no[j]:
                    get_operator_result = operator(int(expression_no[j-1]),int(expression_no[j+1],expression_no[j]))
                    if j+2 > len(expression_no):
                        expression_no = [get_operator_result]
                        # j =
                    else:
                        expression_no = [get_operator_result] + expression_no[j + 2]


    answer = 0
    return answer

def main():
    print(solution("100-200*300-500+20"))


if __name__ == "__main__":
    main()

