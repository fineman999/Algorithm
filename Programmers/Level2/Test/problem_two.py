
# A = line[i][0]
# B = line[i][1]
# E = line[i][2]
# C = line[j][0]
# D = line[j][1]
# F = line[j][2]

def solution(line):
    answer = []
    graph_size_x = [0,0]
    graph_size_y = [0, 0]

    for i in range(len(line)):
        for j in range(i, len(line)):
            if line[i][0]*line[j][1]-line[i][1]*line[j][0] == 0:
                continue
            try:
                x = (line[i][1]*line[j][2] - line[i][2]*line[j][1])/(line[i][0]*line[j][1]-line[i][1]*line[j][0])
                y = (line[i][2]*line[j][0] - line[i][0]*line[j][2])/(line[i][0]*line[j][1]-line[i][1]*line[j][0])
                if int(x) == x and int(y) == y:
                    answer.append([int(x), int(y)])
                    graph_size_x = [max(graph_size_x[0], int(x)), min(graph_size_x[1], int(x))]
                    graph_size_y = [max(graph_size_y[0], int(y)), min(graph_size_y[1], int(y))]
            except:
                continue
    # graph = [["."]*(abs(graph_size_x[0]-graph_size_x[1])+1) for _ in range(abs(graph_size_y[0]-graph_size_y[1])+1)]
    # for ele in answer:
    #     graph[(abs(graph_size_x[0]-graph_size_x[1])+1)//2-ele[1]][ele[0]+(abs(graph_size_y[0]-graph_size_y[1])+1)//2] = "*"
    # graph_answer = []
    # for ele in graph:
    #     graph_answer.append("".join(ele))
    return "hi"


def main():
    print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))


if __name__ == "__main__":
    main()
