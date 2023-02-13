def solution(numbers):
    numbers.sort(reverse=True)
    numbers = list(map(str, numbers))
    n = 2*len(numbers[0])
    answer = []
    for i in range(len(numbers)):
        check = numbers[i]*n
        answer.append([check[:n+1],numbers[i]])

    answer.sort(reverse=True, key=lambda x:x[0])
    result = ""

    for a,b in answer:
        result += b
    return str(int(result))

def main():
    print(solution([12,1213] ))


if __name__ == "__main__":
    main()