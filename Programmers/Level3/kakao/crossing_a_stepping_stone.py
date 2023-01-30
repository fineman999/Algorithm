def binary_search(stones, k, left, right):

    while left <= right:
        mid = (left + right) // 2
        # print(left, right,mid)
        cnt = 0
        for stone in stones:
            # print(cnt)
            if cnt >= k:
                break
            if stone - mid > 0:
                cnt = 0
            else:
                cnt += 1
        if cnt >= k:
            right = mid - 1
        elif cnt < k:
            left = mid + 1
    # print(left,right)
    return left


def solution(stones, k):


    answer = binary_search(stones, k, 1, max(stones))
    return answer


def main():
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


if __name__ == "__main__":
    main()
