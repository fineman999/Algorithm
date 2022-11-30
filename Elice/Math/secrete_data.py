
def calculate(data):

    return str(sum(data))[:10]


def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(int(input()))
    print(calculate(data))

if __name__ == "__main__":
    main()