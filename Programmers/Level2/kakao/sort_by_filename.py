

def calculate_number(file: str):
    file = file.lower()
    before_number = ""
    check_count = 0
    head = ""
    for i in range(len(file)):
        if file[i].isdigit() and check_count < 5:
            before_number += file[i]
            check_count += 1
        else:
            if before_number != "":
                break
            else:
                head += file[i]
    if before_number == "":
        before_number = 0
    else:
        before_number = int(before_number)
    return [head.lower(), before_number]
def solution(files):
    files.sort(key=calculate_number)

    return files


def main():
    print(solution(	["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))


if __name__ == "__main__":
    main()
