import math


def check_prime(number, divisor: list):
    for i in range(2,int(math.sqrt(number))+1):
        if not divisor[i]:
            for j in range(2*i,number+1,i):
                divisor[j] = True
    return divisor


def check_divisor(number, limit, power):
    divisor = set()
    for i in range(1,int(math.sqrt(number))+1):
        if number%i==0:
            divisor.add(i)
            divisor.add(number//i)
        if len(divisor) > limit:
            return power
    return len(divisor)


def solution(number, limit, power):

    prime_numbers = [False]*(number+1)
    prime_numbers = check_prime(number, prime_numbers)

    answer = 1
    for i in range(2,number+1):
        if not prime_numbers[i]:
            answer += 2
        else:
            answer += check_divisor(i,limit, power)

    return answer



def main():
    print(solution(10, 3, 2))


if __name__ == "__main__":
    main()