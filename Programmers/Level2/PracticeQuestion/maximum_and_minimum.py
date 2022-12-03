def solution(s):
    arr = list(map(int, s.split()))
    return f"{min(arr)} {max(arr)}"


def main():
    s = input()
    print(solution(s))


if __name__ == "__main__":
    main()