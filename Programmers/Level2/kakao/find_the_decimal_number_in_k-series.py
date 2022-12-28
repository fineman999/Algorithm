import math
def series(n, k):
    if n < k:
        return str(n)
    remain = n%k
    n = n//k
    return series(n,k) + str(remain)


# def prime(n):
#     prime_number = [False]*(n+1)
#     for i in range(2,n+1):
#         if not prime_number[i]:
#             for j in range(i*2,n+1,i):
#                 if not prime_number[j]:
#                     prime_number[j] = True
#                 if j == n:
#                     return False
#     return True
def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True


def solution(n, k):
    pn = ""
    if k != 10:
        pn = series(n,k)
    else:
        pn = str(n)
    cnt = 0
    arr = pn.split("0")
    for i in range(len(arr)):
        if arr[i] != "1" and arr[i] != "":
            if prime(int(arr[i])):
                cnt += 1

    return cnt




def main():
    print(solution(110011, 10))


if __name__ == "__main__":
    main()
