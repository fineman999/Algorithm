

def valid_twin(weight1, weight2):
    distance = [2,3,4]
    for i in range(3):
        for j in range(3):
            if weight1*distance[i] == weight2*distance[j]:
                # print(weight1, weight2)
                return True
    return False



def solution(weights):
    answer = 0
    # visited = [False]*len(weights)
    # for i in range(len(weights)):
    #     dfs(weights, visited, weights[i])
    for i in range(len(weights)):
        for j in range(i+1, len(weights)):
            if valid_twin(weights[i],weights[j]):
                answer += 1
    return answer