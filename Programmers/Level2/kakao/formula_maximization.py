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
            numbers.append(int(number))
            number = ""
            numbers.append(expression[i])
            operation.add(expression[i])
        else:
            number += expression[i]
    numbers.append(int(number))
    permutations = itertools.permutations(operation, len(operation))
    result = 0
    for permutation in permutations:
        expression_no = deque(numbers)

        for per in permutation:
            stack = deque()
            while expression_no:
                popleft = expression_no.popleft()
                if not stack:
                    stack.append(popleft)
                else:
                    if popleft == per:
                        stack_pop = stack.pop()
                        no_popleft = expression_no.popleft()
                        operator1 = operator(stack_pop, no_popleft, popleft)
                        stack.append(operator1)
                    else:
                        stack.append(popleft)
            expression_no = stack
        result = max(result,abs(expression_no.popleft()))
    return result

def main():
    print(solution("50*6-3*2"))


if __name__ == "__main__":
    main()

