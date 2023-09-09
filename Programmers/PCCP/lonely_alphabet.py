def solution(input_string):
    answer = set()
    temp = set()
    for i in range(len(input_string)-1):
        if input_string[i] != input_string[i+1]:
            if input_string[i] in temp:
                answer.add(input_string[i])
            temp.add(input_string[i])
    if input_string[-1] in temp:
        answer.add(input_string[-1])
        
    if not answer:
        return "N"
    
    result = list(answer)
    result.sort()
    return "".join(result)

def main():
    input_string = input()
    print(solution(input_string))
    

if __name__ == "__main__":
    main()