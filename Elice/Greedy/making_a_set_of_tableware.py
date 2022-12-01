


def calculate(c, s, e):
    for _ in range(e):
        if c//2>=s:
            c-=1
        else:
            s-=1
    if c <= s*2:
        return c//2
    else:
        return s//2




def main():
    c, s, e = map(int, input().split())
    print(calculate(c, s, e))

if __name__ == "__main__":
    main()