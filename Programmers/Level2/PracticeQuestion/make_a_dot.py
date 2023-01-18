def solution(k, d):
    cnt = 0
    j = d
    i = 0
    while i < d+1 and j > -1:
        y = i*k
        x = j*k
        if y**2+x**2 <= d**2:
            cnt += j+1
            i += 1
        else:
            j -= 1
    return cnt


def main():

    return print(solution(2,4))


if __name__ == "__main__":
    main()
