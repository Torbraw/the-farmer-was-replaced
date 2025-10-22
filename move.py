def traverse_grid(start_position, size, func):
    x, y = start_position

    for row in range(size):
        for col in range(size):
            func(x, y)
            if col != size - 1:
                if row % 2 == 0:
                    move(East)
                    x += 1
                else:
                    move(West)
                    x -= 1

        if row != size - 1:
            move(North)
            y += 1


def traverse_grid_reverse(start_position, size, func):
    x, y = start_position

    for row in range(size - 1, -1, -1):
        for col in range(size - 1, -1, -1):
            func(x, y)
            if col != 0:
                if row % 2 == 0:
                    move(West)
                    x -= 1
                else:
                    move(East)
                    x += 1

        if row != 0:
            move(South)
            y -= 1


def traverse_grid_infinite(start_position, size, func):
    x, y = start_position

    while True:
        traverse_grid((x, y), size, func)
        traverse_grid_reverse((x, y + size - 1), size, func)


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
