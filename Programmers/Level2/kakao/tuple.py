def solution(s):
    string = s[1:-1]
    string_tuple = []
    insert_string = []
    insert_number = ""
    for i in range(len(string)):
        if string[i] == "{":
            insert_string = []
            insert_number = ""
            continue
        if string[i].isdigit():
            insert_number += string[i]
            # insert_string.append(int(string[i]))
            continue
        if string[i] == ",":
            insert_string.append(int(insert_number))
            insert_number = ""
            continue
        if string[i] == "}":
            insert_string.append(int(insert_number))
            string_tuple.append(insert_string)
    string_tuple.sort(key=lambda x: len(x))
    result = []
    for elements in string_tuple:
        for ele in elements:
            if ele not in result:
                result.append(ele)

    return result


def main():
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))


if __name__ == "__main__":
    main()
