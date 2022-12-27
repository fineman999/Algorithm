
def solution(n, left, right):
    arr = []
    for i in range(left, right+1):
        y = i//n
        x = i%n
        arr.append(max(x,y)+1)
    return arr




def main():
    print(solution(3, 2, 5))


if __name__ == "__main__":
    main()
