def single(number):
    return number

def double(number):
    return number**2

def triple(number):
    return number**3

def star(number):
    return number*2

def acha(number):
    return -number

def solution(dartResult):
    answer = int(dartResult[0])
    result = 0
    for i in range(1, len(dartResult)):

        if dartResult[i] == "S":
            answer = single(answer)
        elif dartResult[i] == "D":
            answer = double(answer)
        elif dartResult[i] == "T":
            answer = triple(answer)
        elif dartResult[i].isdigit():
            result += answer
            answer = int(dartResult[i])
        elif dartResult[i] == "*":
            answer = double(answer)

    return answer

def main():
    print(solution("1S2D*3T"))


if __name__ == "__main__":
    main()
