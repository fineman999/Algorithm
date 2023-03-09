import sys
sys.setrecursionlimit(10**6)
consonants = ['a','e','i','o','u']

answer = []
def dfs(L, C, alpha, consonants_cnt, vowels_cnt, cnt, result, index):
    if L == cnt:
        if consonants_cnt >= 1 and vowels_cnt >=2:
            global answer
            answer.append(result)
        return

    for i in range(index, C):
        if alpha[i] in consonants:
            dfs(L, C, alpha, consonants_cnt + 1, vowels_cnt, cnt + 1, result + alpha[i], i+1)
        else:
            dfs(L, C, alpha, consonants_cnt, vowels_cnt+1, cnt + 1, result + alpha[i], i+1)



def solution(L, C, alpha):
    alpha.sort()
    # 최소 한개의 모음, 최소 두개 의 모음

    dfs(L, C, alpha, 0, 0, 0 , "", 0)
    for ele in answer:
        print(ele)



def main():
    L, C = map(int ,sys.stdin.readline().rstrip().split())
    alpha = list(sys.stdin.readline().rstrip().split())
    solution(L, C, alpha)

if __name__ == '__main__':
    main()