
arr = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def direction(x,y,k):
    global arr
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1<nx<5 and -1<ny<5:
            if arr[k][ny][nx] == 'P' or arr[k][ny][nx] == 'K':
                return False
            if arr[k][ny][nx] == 'O':
                arr[k][ny][nx] = 'K'
    return True

def solution(places):
    global arr
    for place in places:
        new_arr = []
        for ele in place:
            new_arr.append(list(ele))
        arr.append(new_arr)
    answer = []

    for k in range(len(arr)):
        valid = True
        for i in range(5):
            for j in range(5):
                if arr[k][i][j] == 'P':
                    if not direction(j,i,k):
                        valid = False
                        break
        if valid:
            answer.append(1)
        else:
            answer.append(0)


    return answer


def main():

    return print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))


if __name__ == "__main__":
    main()
