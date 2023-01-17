import itertools

def checkValid(check_i, combi):
    final_valid = True
    for element in check_i:
        valid = True
        for k in range(len(element)):
            # false 되면 다른거
            if element[k] not in combi:
                valid = False
                break
        if valid:
            final_valid = False
            break
    return final_valid

def solution(relation):
    answer = 0
    check_i = []
    for i in range(1,len(relation[0])+1):

        combinations = itertools.combinations(range(len(relation[0])), i)
        for combi in combinations:
            combi = list(combi)

            if not checkValid(check_i, combi):
                continue
            # print(check_i, combi)
            check_column = []
            for j in range(len(relation)):
                check = []
                for element in combi:
                    check.append(relation[j][element])
                check = tuple(check)
                check_column.append(check)
            if len(check_column) == len(set(check_column)):
                # print(check_column)
                answer += 1
                check_i.append(combi)
    # print(check_i)
    return answer

def main():

    return print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))


if __name__ == "__main__":
    main()
