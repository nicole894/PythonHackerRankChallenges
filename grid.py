def grid(dimensions, x, y, path):

    for direction in path:
        if direction == 'L':
            if y-1 < 0:
                y = dimensions-1
            else:
                y -= 1

        if direction == 'R':
            if y+1 == dimensions:
                y = 0
            else:
                y += 1

        if direction == 'U':
            if x-1 >= 0:
                x -= 1

        if direction == 'D':
            if x + 1 < dimensions:
                x += 1

    final_position = [x, y]

    return final_position