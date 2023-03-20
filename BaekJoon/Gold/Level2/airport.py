import sys

parents = []
def find_parents(air):
    start = air
    while air != parents[air]:
        air = parents[air]
    parents[start] = air
    return air

def solution(G, P, airs):
    global parents
    parents = [i for i in range(G+1)]
    cnt = 0
    for air in airs:
        check = find_parents(air)
        if find_parents(air) > 0:
            parents[check] -= 1
        else:
            return cnt
        cnt += 1
    return cnt

def main():
    G = int(sys.stdin.readline())
    P = int(sys.stdin.readline())
    airs = []
    for _ in range(P):
       airs.append(int(sys.stdin.readline()))
    print(solution(G, P, airs))

if __name__ == '__main__':
    main()