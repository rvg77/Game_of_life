import argparse
import Modeling_lib
import sys


def parse_input(f):
    n = int(f.readline())
    h, w = map(int, f.readline().split(' '))

    ocean = [[None] * w for j in range(h)]

    for i in range(h):

        line = f.readline()
        for j in range(w):
            if line[j] == 'F':
                ocean[i][j] = Modeling_lib.Fish()
            elif line[j] == 'C':
                ocean[i][j] = Modeling_lib.Crayfish()
            elif line[j] == '.':
                ocean[i][j] = Modeling_lib.Void()
            elif line[j] == '#':
                ocean[i][j] = Modeling_lib.Rock()
    return n, h, w, ocean


parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', nargs='?', const='sys.stdin', default='sys.stdin',
                    help='Use -i/--input + filename to read from file(default=sys.stdout).')

parser.add_argument('-o', '--output', nargs='?', const='sys.stdout', default='sys.stdout',
                    help='Use -o/--output + filename to read from file(default=sys.stdout).')

res = parser.parse_args()

if parser.parse_args().input != 'sys.stdin':
    with open(parser.parse_args().input, 'r') as file:
        n, h, w, ocean = parse_input(file)
else:
    n, h, w, ocean = parse_input(sys.stdin)

first_gen = Modeling_lib.Generation(h, w, False)

first_gen.set_ocean(ocean)

life = Modeling_lib.Life(first_gen)

if parser.parse_args().output != 'sys.stdout':
    with open(parser.parse_args().output, 'w') as file:
        file.write(life.get_generation(n).print_gen())
else:
    sys.stdout.write(life.get_generation(n).print_gen())
