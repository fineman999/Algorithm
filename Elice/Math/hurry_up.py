
def calculate(n):
    minute = sum(n)//60
    seconds = sum(n)%60
    return minute, seconds

def main():
    n = []
    for i in range(4):
        n.append(int(input()))

    minute, second = calculate(n)
    print(minute)
    print(second)

if __name__ == "__main__":
    main()