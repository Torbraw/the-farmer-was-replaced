def traverse_grid(start_position, size, func):
    x, y = start_position

    for row in range(size):
        for _ in range(size):
            func(x, y)
            if _ != size - 1:
                if row % 2 == 0:
                    move(East)
                    x += 1
                else:
                    move(West)
                    x -= 1

        if row != size - 1:
            move(North)
            y += 1


def go_to_position(position):
    target_x, target_y = position
    while get_pos_x() > target_x:
        move(West)
    while get_pos_x() < target_x:
        move(East)
    while get_pos_y() > target_y:
        move(South)
    while get_pos_y() < target_y:
        move(North)
