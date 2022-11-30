
def calculate(num1, num2):
    return int(str(num1)[::-1]) + int(str(num2)[::-1])


def main():
    num1, num2 = map(int, input().split())
    print(calculate(num1,num2))


if __name__ == "__main__":
    main()