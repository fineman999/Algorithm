
def calculate(N, K, arr):
    answer = []
    start = sorted(arr[:K], reverse=True)
    answer.append(start[-1])

    for i in range(K,N):
        if answer[-1] >= arr[i]:
            answer.append(answer[-1])
        else:
            answer.append(sorted(arr[:i+1], reverse=True)[K-1])

    return " ".join(map(str, answer))

def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(calculate(N, K, arr))


if __name__ == "__main__":
    main()