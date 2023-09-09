
import heapq    
from collections import deque 
def solution(program):
    answer = [0 for _ in range(10)]
    
    program.sort(key = lambda x:x[1])
    
    program = deque(program)
    waitq = []
    
    time = 0
    valid = True
    while valid:
        while program and program[0][1] <= time:
            heapq.heappush(waitq, program.popleft())
            
        if waitq:
            priority, start_time, run_time  = heapq.heappop(waitq)
            answer[priority] += time - start_time
            time += run_time
        
        if not program and not waitq:
            valid = False
        
        
        if program and program[0][1] > time:
            time = program[0][1]

        
    answer[0] = time
        
    return answer

def main():
    inputs = [[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]
    print(solution(program=inputs))


if __name__ == "__main__":
    main()