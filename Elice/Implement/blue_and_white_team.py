def competition(blue, white):
    return max(sum(blue),sum(white))



def main():
    blue = list(map(int, input().split()))
    white = list(map(int, input().split()))

    print(competition(blue,white))

if __name__ == "__main__":
    main()