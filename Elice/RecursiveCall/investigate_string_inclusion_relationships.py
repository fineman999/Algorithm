import sys
sys.setrecursionlimit(100000)

def strContain(A, B) :
    '''
    문자열 A의 알파벳이 문자열 B에 모두 포함되어 있으면 "Yes", 아니면 "No"를 반환합니다.
    '''
    for ele in A:
        if not ele in B:
            return "NO"
    return "YES"

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    A = input()
    B = input()

    print(strContain(A, B))

if __name__ == "__main__":
    main()
