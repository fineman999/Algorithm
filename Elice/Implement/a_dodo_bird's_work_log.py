def calculator(n,b):
    a = []
    a.append(b[0])
    for i in range(1,n):
        a.append(b[i]*(i+1)-sum(a))
    return " ".join(list(map(str, a)))

def main():
    n = int(input())
    B = list(map(int, input().split()))
    print(calculator(n, B))


if __name__ == "__main__":
    main()