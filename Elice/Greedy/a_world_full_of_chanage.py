moneys = [1_000, 100, 10, 1]
def calculate(n):
    i = 0
    cnt = 0
    n = 10_000 - n
    while True:
        if n < 1:
            break
        if moneys[i] > n:
            i += 1
        else:
            cnt += 1
            n -= moneys[i]
    return cnt



def main():
    n = int(input())
    print(calculate(n))

if __name__ == "__main__":
    main()