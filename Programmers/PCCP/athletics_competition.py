
def dfs(ability, answer, depth, visited, m, n):

    if depth == n:
        return answer
    
    result = 0
    for i in range(m):
        if not visited[i]:
            visited[i] = True
            result = max(result, dfs(ability, answer + ability[i][depth], depth + 1, visited, m, n))
            visited[i] = False
    return result

                         
def solution(ability):
    
    answer = 0
    m = len(ability) # 사람들
    n = len(ability[0]) # 종목
    visited = [False] * m
    
    answer = dfs(ability, 0, 0, visited, m, n)
        
    return answer