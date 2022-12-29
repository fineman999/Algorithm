nx = [1,0,-1,0]
ny = [0,-1,0,1]


def solution(dirs):
    direction = {"U":(nx[3],ny[3]), "D":(nx[1],ny[1]),
                 "R":(nx[0],ny[0]), "L":(nx[2],ny[2])}
    visited_coordinate = []
    state_coordinate = [0,0]
    for i in range(len(dirs)):
        (x,y) = direction.get(dirs[i])
        start_x = state_coordinate[0]
        start_y = state_coordinate[1]
        start_x += x
        start_y += y
        if -5 <= start_x <= 5 and -5<= start_y <= 5:
            if (state_coordinate[0],state_coordinate[1], start_x,start_y) not in visited_coordinate\
                    and (start_x,start_y, state_coordinate[0],state_coordinate[1]) not in visited_coordinate:
                visited_coordinate.append((state_coordinate[0],state_coordinate[1],
                                           start_x,start_y))
            state_coordinate[0] = start_x
            state_coordinate[1] = start_y

    return len(visited_coordinate)


def main():
    print(solution("ULURRDLLU"))


if __name__ == "__main__":
    main()