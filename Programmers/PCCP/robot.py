dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(command):
    answer = [0, 0]
    
    direct = 0
    for i in range(len(command)):
        if command[i] == "R":
            direct = (direct + 1) % 4
        elif command[i] == "L":
            direct = (direct + 3) % 4
        elif command[i] == "G":
            answer[0] += dx[direct]
            answer[1] += dy[direct]
        else:
            answer[0] -= dx[direct]
            answer[1] -= dy[direct]
        
    return answer

def main():
    inputs = "GRGLGRG"
    print(solution(command=inputs))
    
if __name__ == "__main__":
    main()