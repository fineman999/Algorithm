def recursive(arr):
    check_arr = []

    for ele in arr:
        for j in ele:
            check_arr.append(j)

    n = len(arr)
    if len(check_arr) == 1:
        return [check_arr.count(0), check_arr.count(1)]

    if 0 not in check_arr:
        return [0, 1]
    if 1 not in check_arr:
        return [1, 0]

    answer = [0,0]
    direction = [[0,n//2, 0, n//2], [0, n//2, n//2, n],
                 [n//2,n, 0 ,n//2], [n//2,n, n//2,n]]
    for i in range(4):
        new_arr = []
        for j in range(direction[i][0], direction[i][1]):
            arr_x = []
            for k in range(direction[i][2], direction[i][3]):
                arr_x.append(arr[j][k])
            new_arr.append(arr_x)
        answer_check = recursive(new_arr)

        answer[0] += answer_check[0]
        answer[1] += answer_check[1]
    return answer


def solution(arr):
    n = len(arr)
    if n == 1:
        return [arr.count(0), arr.count(1)]

    return recursive(arr)



def main():
    print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))


if __name__ == "__main__":
    main()
