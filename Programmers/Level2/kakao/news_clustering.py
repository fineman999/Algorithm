import math
def changeArr(str):
    arr = []
    for i in range(0,len(str)-1):
        if not str[i:i+2].isalpha():
            continue
        arr.append(str[i:i+2].upper())
    return arr
def solution(str1, str2):
    arr1 = changeArr(str1)
    arr2 = changeArr(str2)
    intersection = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                intersection += 1
                arr2.pop(j)
                break
    answer = 1
    if intersection == 0 and (len(arr2)+len(arr1))==0:
        return answer*65536
    answer = math.trunc(intersection/(len(arr2)+len(arr1))*65536)
    return answer

def main():

    print(solution("aa1+aa2", "AAAA12"))


if __name__ == "__main__":
    main()
