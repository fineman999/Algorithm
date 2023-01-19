import math
def gcd(a,b):
    # while b>0:
    #     a, b = b, a%b
    # if a <= 1:
    #     return 0
    # return a
    return math.gcd(a,b)

def recursive(array):
    if len(array) == 1:
        return array[0]
    answer = gcd(array[0],array[1])
    if answer == 0:
        return 0
    for i in range(2,len(array)):
        answer = gcd(answer, array[i])
        if answer == 0:
            return 0
    return answer

def condition(number, array):
    valid = True
    for element in array:
        if element%number == 0:
            valid = False
            break
    if valid:
        return True
    return False


def solution(arrayA, arrayB):
    answer = 0
    # print(gcd(17,12))
    check_A = recursive(arrayA)
    # type 1
    if check_A:
        if condition(check_A,arrayB):
            answer = max(check_A,answer)
    else:
        if 1 in arrayA:
            if condition(1, arrayB):
                answer = max(1, answer)
    check_B = recursive(arrayB)

    if check_B:
        if condition(check_B,arrayA):
            answer = max(check_B,answer)
    else:
        if 1 in arrayB:
            if condition(1, arrayA):
                answer = max(1, answer)

    return answer
def main():
    return print(solution([20,40,10],[1,17]))


if __name__ == "__main__":
    main()