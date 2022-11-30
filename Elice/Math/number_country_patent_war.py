
def calculate(n):
    cnt = 0
    for i in range(1,n):
        if i%3==0 or i%5==0:
           cnt+=i
    return cnt


def main():
    n = int(input())
    print(calculate(n))

if __name__ == "__main__":
    main()