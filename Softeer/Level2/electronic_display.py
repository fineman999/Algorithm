import sys

diary = {'0': '1110111',
         '1': '0010010',
         '2': '1011101',
         '3': '1011011',
         '4': '0111010',
         '5': '1101011',
         '6': '1101111',
         '7': '1110010',
         '8': '1111111',
         '9': '1111011',
         ' ': '0000000'}


def solution(T: int, arr: list):
    answer = []
    for A, B in arr:
        cnt = 0
        A = str(A)
        B = str(B)
        A = ' ' * (5 - len(A)) + A
        B = ' ' * (5 - len(B)) + B

        for i in range(5):
            diary_A = diary[A[i]]
            diary_B = diary[B[i]]
            for j in range(7):
                if diary_A[j] != diary_B[j]:
                    cnt += 1

        answer.append(cnt)
    return answer


def main():
    T = int(sys.stdin.readline())
    arr = []
    for i in range(T):
        arr.append(list(map(int, sys.stdin.readline().split())))

    answer = solution(T, arr)
    for element in answer:
        print(element)


if __name__ == "__main__":
    main()

