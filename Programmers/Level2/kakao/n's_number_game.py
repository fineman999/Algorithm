change_number = {10: 'A', 11: 'B', 12: 'C',13: 'D',14: 'E', 15: 'F'}

def radix_number(n,k):
    if n < k:
        if 10 <= n <= 15:
            return change_number[n]
        return str(n)
    remain = n % k
    if 10 <= remain <= 15:
        remain = change_number[remain]
    return radix_number(n//k, k) +str(remain)


def solution(n, t, m, p):
    answer = ''
    result = ""
    for i in range(t*m):
        result += radix_number(i,n)
        if len(result) >= t*m:
            for i in range(t):
                answer += result[i*m+p-1]
            break

    return answer


def main():
    print(solution(2, 4, 2, 1))


if __name__ == "__main__":
    main()
