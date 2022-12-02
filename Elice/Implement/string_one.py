
def calculate(s, t):
    if s in t:
        return 1
    return 0


def main():
    s = input()
    t = input()
    print(calculate(s, t))


if __name__ == "__main__":
    main()