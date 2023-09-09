
def solution(queries):
    answer = []
    
    for y, x in queries:
        parent = "Rr"
 
        x -= 1
        
        stack = []
        
        for _ in range(1, y):
            stack.append(x%4)
            x = x//4
            
        while stack:
            temp = stack.pop()
            if parent == "Rr":
                if temp == 0:
                    parent = "RR"
                elif temp == 3:
                    parent = "rr"
                else:
                    parent = "Rr"
            else:
                break
        answer.append(parent)
    
    return answer

def main():
    queries =	[[3, 1], [2, 3], [3, 9]]
    print(solution(queries=queries))
    
    
    
if __name__ == "__main__":
    main()