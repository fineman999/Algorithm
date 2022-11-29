def chef(times, T):
    answer = 0
    for i in range(len(times)):
        answer += times[i]
        if answer >= T:
            return i
    if answer == 0:
        return 0
    return len(times)
def main():
    N, T = map(int, input().split())
    times = list(map(int, input().split()))
    print(chef(times, T))



if __name__ =="__main__":
    main()