
def calculate(n):
    cnt = 1

    for i in range(n):
        cnt = cnt*2
    cnt = str(cnt)
    return sum(list(map(int, cnt)))


def main():
    n = int(input())
    print(calculate(n))

if __name__ == "__main__":
    main()