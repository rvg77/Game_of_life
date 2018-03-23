import Modeling_lib


def get_inf(lines):
    n = int(lines[0])
    h, w = map(int, lines[1].split(' '))

    ocean = [[None] * w for j in range(h)]

    for i in range(2, len(lines)):

        line = lines[i]
        for j in range(w):
            if line[j] == 'F':
                ocean[i - 2][j] = Modeling_lib.Fish()
            elif line[j] == 'C':
                ocean[i - 2][j] = Modeling_lib.Crayfish()
            elif line[j] == '.':
                ocean[i - 2][j] = Modeling_lib.Void()
            elif line[j] == '#':
                ocean[i - 2][j] = Modeling_lib.Rock()

    return n, h, w, ocean
