
graph =[]
def integration(k):
    global graph
    while k > 1:
        before = k
        if k%2==0:
            k = k/2
        else:
            k = k*3 + 1
        if graph:
            graph.append(graph[-1]+(before+k)/2)
        else:
            graph.append((before+k)/2)


def solution(k, ranges):
    answer = []
    global graph
    graph.append(0)
    integration(k)
    n = len(graph) -1
    for ran in ranges:
        [first, second] = ran
        if n + second < first:
            answer.append(-1.0)
        else:
            answer.append(graph[n+second] - graph[first])
    return answer

def main():
    print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]))


if __name__ == "__main__":
    main()