from collections import deque

def solution(menu, order, k):
    answer = 0
    
    
    order = deque(order)
    waitq = deque()
    time = 0
    warking = False
    run_time = 0
    while order:
        if run_time == time and waitq:
            warking = False
            waitq.popleft()
        
        if time % k == 0:
            waitq.append(order.popleft())
            
        if not warking and waitq:
            run_time = menu[waitq[0]] + time
            warking = True
        
            
        answer = max(answer, len(waitq))
        time += 1
        
    return answer

def main():
    menu = [5, 12, 30]	
    order = [1, 2, 0, 1]
    k = 10
    print(solution(menu=menu, order=order, k=k))

    


if __name__ == "__main__":
    main()