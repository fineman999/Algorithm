from itertools import permutations
import math


def get_prime_numbers(number: int):
    valid = [False] * (number + 1)
    valid[0] = True
    valid[1] = True

    for i in range(2, int(math.sqrt(number + 1)) + 1):
        if not valid[i]:
            for j in range(i * 2, len(valid), i):
                valid[j] = True
    return valid


def solution(numbers):
    numbers = list(numbers)

    cnt = 0
    answer = set()
    for j in range(1, len(numbers) + 1):
        for i in permutations(numbers, j):
            answer.add(int("".join(i)))

    valid = get_prime_numbers(int("".join(str(max(answer)))))
    # print(answer)
    while answer:
        if not valid[answer.pop()]:
            cnt += 1
    return cnt


def main():
    print(solution("1000"))


if __name__ == "__main__":
    main()
