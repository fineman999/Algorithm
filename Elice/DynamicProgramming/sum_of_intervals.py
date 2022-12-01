import math
def calculate(arr, s, n):
    sums = [0]*n
    counts = [0]*n
    sums[0] = arr[0]
    counts[0] = 1
    min_result = 10001
    for i in range(1, len(arr)):
        if sums[i-1]+arr[i] < s:
            sums[i] = sums[i-1]+arr[i]
            counts[i] = counts[i-1] + 1
        elif sums[i-1] + arr[i] > s:
            start = arr[i]
            cnt = 1
            sums[i] = sums[i - 1] + arr[i]
            counts[i] = counts[i - 1] + 1
            if start >= s:
                counts[i] = 1
                sums[i] = start
                min_result = min(counts[i], min_result)
            else:
                for j in range(i-1,-1,-1):
                    start += arr[j]
                    cnt += 1
                    if start >= s:
                        counts[i] = cnt
                        sums[i] = start
                        min_result = min(counts[i], min_result)
                        break
        else:
            counts[i] = counts[i-1] + 1
            sums[i] = sums[i-1]+arr[i]
            min_result = min(counts[i], min_result)
    if min_result == 10001:
        return 0
    return min_result



def main():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    print(calculate(arr, s, n))

if __name__ == "__main__":
    main()