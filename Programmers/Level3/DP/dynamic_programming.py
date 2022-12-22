result = 0

def dfs(triangle, depth, row):
    global result
    if len(triangle)-1 == depth:
        return triangle[depth][row]
    left = dfs(triangle, depth + 1, row)
    right = dfs(triangle, depth + 1, row + 1)
    return triangle[depth][row] + max(left, right)


def dfsV(triangle, depth, row):
    for i in range(1,len(triangle)):
        for j in range(0, len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])

def solution(triangle):

    return dfsV(triangle, 0, 0)


def main():

    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


if __name__ == "__main__":
    main()
