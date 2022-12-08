def solution(n):
    cnt = 1

    while n != 1:
        if n % 2 == 1:
            n-=1
            cnt += 1
        n = n//2
    return cnt

# def solution(n):
#
#     answer = [0, 1, 1]
#     for i in range(3, 10):
#         if i%2 == 1:
#             answer.append(answer[-1]+1)
#         else:
#             answer.append(answer[i//2])
#     if n%2 == 0:
#
#     return answer[-1]




def main():
    print(solution(5000))


if __name__ == "__main__":
    main()
