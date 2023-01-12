result = []

def recursive(answer, query):
    global result
    [y1, x1, y2, x2] = query
    row = x2 - x1
    column = y2 - y1
    direction = [[1,0,row], [0,1,column], [-1,0,row], [0,-1,column]]

    start_x = x1-1
    start_y = y1-1

    cnt = answer[start_y+1][start_x]
    cnt_min = cnt
    for i in range(4):
        for j in range(direction[i][2]):
                cnt_2 = answer[start_y][start_x]
                answer[start_y][start_x] = cnt
                cnt = cnt_2
                start_x += direction[i][0]
                start_y += direction[i][1]
                cnt_min = min(cnt, cnt_min)
    result.append(cnt_min)
    return answer



def solution(rows, columns, queries):
    answer = []
    global result

    for row in range(rows):
        answer.append([columns*row + column for column in range(1,columns+1)])
    for query in queries:
        answer = recursive(answer, query)


    return result


def main():
    print(solution(3,4, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))


if __name__ == "__main__":
    main()