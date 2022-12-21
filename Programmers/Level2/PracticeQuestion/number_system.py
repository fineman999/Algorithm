numbers = ['1','2','4']
def convert(n):
    global numbers
    q,r = divmod(n,3)
    if r == 0:
        q-=1

    if q == 0:
        return numbers[r-1]
    return convert(q) + numbers[r-1]

def solution(n):
    global numbers
    answer = ['1','2','4']
    # before_number = 0
    # for i in range(3, n+1,3):
    #     # if i % 3 == 0:
    #     #     before_number += 1
    #     answer.append(answer[before_number]+numbers[i%3])
    #     answer.append(answer[before_number] + numbers[i % 3+1])
    #     answer.append(answer[before_number] + numbers[i % 3+2])
    #     before_number += 1

    return convert(n)


def main():
    print(solution(6))


if __name__ == "__main__":
    main()
