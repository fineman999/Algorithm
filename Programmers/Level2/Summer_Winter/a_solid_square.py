def divide(w,h):
    for i in range(min(w,h),0,-1):
        if w%i == 0 and h%i == 0:
            return i

def solution(w,h):
    if w == h:
        return w*h-w
    big_w = w
    big_h = h

    lcm = divide(w,h)
    w = w // lcm
    h = h // lcm
    cnt = 0
    arr = [[0] * (w+1) for _ in range(h+1)]

    for j in range(0, h+1):
        for i in range(0, w//2+1):
            if j*w > i*h:
                arr[j][i] = 1
            elif j*w < i*h:
                arr[j][i] = -1
            else:
                arr[j][i] = 0

    # for j in range(0, h):
    # for j in range(0, h):
    #     if j*w > 1*h:
    #         arr[j][1] = 1
    #     elif (j+1)*w < 0:
    #         arr[j+1][0] = -1
    #     if arr[j][1] + arr[j+1][0] == 0:
    #         cnt += 1
    # cnt = cnt*2
    return big_h*big_w - cnt*lcm

def main():
    print(solution(8, 12))


if __name__ == "__main__":
    main()
