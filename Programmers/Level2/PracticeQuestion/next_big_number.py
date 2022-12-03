def solution(n):
    count_zero = bin(n).count("1")
    while True:
        n += 1
        if bin(n).count("1") == count_zero:
            return n


def main():
    s = int(input())
    print(solution(s))


if __name__ == "__main__":
    main()
