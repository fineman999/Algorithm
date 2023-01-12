
def solution(A, B):
    A.sort()
    B.sort()
    i = 0
    cnt = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[j] < B[i]:
            cnt += 1
            i += 1
            j += 1
        else:
            i += 1

    return cnt




def main():
    print(solution([5,1,3,7], [2,2,6,8]))


if __name__ == "__main__":
    main()