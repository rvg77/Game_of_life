import argparse
import Modeling_lib
import sys
import Parse_input

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', nargs='?', const='sys.stdin', default='sys.stdin',
                    help='Use -i/--input + filename to read from file(default=sys.stdout).')

parser.add_argument('-o', '--output', nargs='?', const='sys.stdout', default='sys.stdout',
                    help='Use -o/--output + filename to read from file(default=sys.stdout).')

res = parser.parse_args()

if parser.parse_args().input != 'sys.stdin':
    with open(parser.parse_args().input, 'r') as file:
        lines = file.read().split('\n')
        n, h, w, ocean = Parse_input.get_inf(lines)
else:
    lines = sys.stdin.read().split('\n')
    n, h, w, ocean = Parse_input.get_inf(lines)

first_gen = Modeling_lib.Generation(h, w, False)

first_gen.set_ocean(ocean)

life = Modeling_lib.Life(first_gen)

if parser.parse_args().output != 'sys.stdout':
    with open(parser.parse_args().output, 'w') as file:
        file.write(life.get_generation(n).print_gen())
else:
    sys.stdout.write(life.get_generation(n).print_gen())
