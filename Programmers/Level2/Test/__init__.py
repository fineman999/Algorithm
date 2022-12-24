def solution(s):
    answer = list(map(int, s.split()))

    return f"{min(answer)} {max(answer)}"


def main():
    print(solution("1 2 3 4"))


if __name__ == "__main__":
    main()
