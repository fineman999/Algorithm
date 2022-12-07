def solution(numbers):

    numbers.sort()
    cnt = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            for k in range(j+1,len(numbers)):

                if numbers[i] + numbers[j] + numbers[k]== 0:
                    cnt += 1
    return cnt




def main():
    number = [-2, 3, 0, 2, -5]
    print(solution(number))


if __name__ == "__main__":
    main()
