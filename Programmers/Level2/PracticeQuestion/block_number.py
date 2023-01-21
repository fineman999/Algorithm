import math
def recursive(number: int) -> int:
    for i in range(2, int(math.sqrt(number))+1):
        if number%i==0 and number//i <= 10_000_000:
            return number//i
    return 1

def solution(begin, end):
    minus= end-begin
    answer = [0]*(minus+1)
    start = begin
    if begin == 1:
        start += 1

    for i in range(start,end+1):
        answer[i - begin] = recursive(i)
    return answer

def main():
    print(solution(1,10))


if __name__ == "__main__":
    main()