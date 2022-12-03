# def solution(s):
#     arr = s.split()
#     result = []
#     for ele in arr:
#         if not ele[0].isalpha():
#             result.append(ele)
#         else:
#             result.append(ele[0].upper()+ele[1:].lower())
#     return " ".join(result)
def solution(s):
    arr = []
    if s[0].isalpha():
        arr.append(s[0].upper())
    else:
        arr.append(s[0])
    for i in range(1,len(s)):
        if s[i].isalpha():
            if s[i-1] == " ":
                arr.append(s[i].upper())
            else:
                arr.append(s[i].lower())
        else:
            arr.append(s[i])
    return "".join(arr)



def main():
    s = input()
    print(solution(s))


if __name__ == "__main__":
    main()