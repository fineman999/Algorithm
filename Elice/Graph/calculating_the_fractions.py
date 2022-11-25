import sys
from collections import deque

sys.setrecursionlimit(100000)

def SNS(n_nodes, myInput, a, b):
    '''
    엘리스친구의 친구관계가 myInput으로 주어지고, 사용자 a, b가 주어질 때 둘 사이의 촌수를 반환합니다.
    '''
    return 0

def main():

    N, M = map(int, input().split())
    users = [-1]*N
    user_1, user_2 = map(int, input().split())
    for i in range(M):
        user, relation = map(int, input().split())



if __name__ == "__main__":
    main()