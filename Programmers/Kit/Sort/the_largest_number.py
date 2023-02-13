



def solution(numbers):
    numbers.sort(reverse=True)
    numbers = list(map(str, numbers))
    n = len(numbers[0])
    answer = []
    for i in range(len(numbers)):
        if n - len(numbers[i]) > 0:
            check = numbers[i]*n
            answer.append([check[:n],numbers[i]])
        else:
            answer.append([numbers[i],numbers[i]])
    answer.sort(reverse=True, key=lambda x:x[0])
    result =""
    # print(answer)
    for a,b in answer:
        result += b
    return int(result)

def main():
    print(solution([12, 1213] ))


if __name__ == "__main__":
    main()