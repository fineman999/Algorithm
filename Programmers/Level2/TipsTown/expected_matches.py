import math
def recursion(n,a,b):
    cnt = 0
    while n>=2:
        if b-a == 1 and b%2==0:
            cnt += 1
            break
        cnt +=1
        b = math.ceil(b/2)
        a = math.ceil(a/2)
        n = n//2
    return cnt
def solution(n,a,b):
    if a<b:
        return recursion(n,a,b)
    return recursion(n,b,a)



def main():
    n = 16
    a = 9
    b= 12
    print(solution(n,a,b))


if __name__ == "__main__":
    main()
