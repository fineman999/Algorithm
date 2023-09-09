import math
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

sub_answer = math.inf
    
def bfs(graph, visited, n, m):
    global sub_answer
    q = deque()
    q.append((0,0,False))
    visited[0][0][0] = True
    cnt = 1
    while q:
        for i in range(len(q)):
            (x, y, used) = q.popleft()
            
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                
                
                if -1 < ny < n and -1 < nx < m and not visited[ny][nx][used]:
                    if graph[ny][nx] == 0:
                        if nx == m -1 and ny == n - 1:
                            sub_answer = cnt
                            return
                        visited[ny][nx][used] = True
                        q.append((nx, ny, used))
                        
                if not used:
                    nx += dx[i]
                    ny += dy[i]
                    if -1 < ny < n and -1 < nx < m and not visited[ny][nx][1]:
                        if graph[ny][nx] == 0:
                            if nx == m -1 and ny == n - 1:
                                sub_answer = cnt
                                return
                            visited[ny][nx][1] = True
                            q.append((nx, ny, True))
        cnt += 1        

    
def solution(n, m, hole):
    global sub_answer
    graph = [[0]*m for i in range(n)]
    
    for a,b in hole:
        graph[a-1][b-1] = 1
    

    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    

    bfs(graph, visited, n, m)

    
    if sub_answer == math.inf:
        return -1
    
    return sub_answer


def main():
    n = 5
    m= 4
    hole =  [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]
    
    print(solution(n=n, m=m, hole=hole))
    
if __name__ == "__main__":
    main()