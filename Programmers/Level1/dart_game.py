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
    answer_sum = []
    for i in range(1, len(dartResult)):

        if dartResult[i] == "S":
            answer = single(answer)
        elif dartResult[i] == "D":
            answer = double(answer)
        elif dartResult[i] == "T":
            answer = triple(answer)
        elif dartResult[i].isdigit():
            if dartResult[i] == "0":
                if dartResult[i-1] == "1":
                    answer = 10
                    continue
            answer_sum.append(answer)
            answer = int(dartResult[i])
        elif dartResult[i] == "*":

            answer = star(answer)
            try:
                answer_sum[-1] = answer_sum[-1]*2
            except:
                continue
        else:
            answer = acha(answer)
    answer_sum.append(answer)
    return sum(answer_sum)

def main():
    print(solution("1D2S#10S"))


if __name__ == "__main__":
    main()
