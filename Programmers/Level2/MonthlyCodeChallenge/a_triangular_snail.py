def solution(n):
    answer = []
    for i in range(1,n+1):
        answer.append([0 for _ in range(i)])
    x,y = 0,-1
    cnt = 0
    for i in range(n):
        for j in range(i,n):
            if i%3==0:
               y += 1
            elif i%3==1:
                x += 1
            else:
                y -= 1
                x -= 1
            cnt += 1
            answer[y][x] = cnt
    result = []
    for ele in answer:
        for i in ele:
            result.append(i)
    return result



def main():
    print(solution(4))


if __name__ == "__main__":
    main()