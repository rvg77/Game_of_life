import Modeling_lib
import os

tests = 100
for test_n in range(tests):
    file = open('./Tests/TESTinput_' + str(test_n) + '.txt')
    lines = file.read().split('\n')
    file.close()
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

    first_gen = Modeling_lib.Generation(h, w, False)

    first_gen.set_ocean(ocean)

    life = Modeling_lib.Life(first_gen)

    file = open('./Tests/TESTmyoutput_' + str(test_n) + '.txt', 'w')
    file.write(life.get_generation(n).print_gen())
    file.close()

    if open('./Tests/TESTmyoutput_' + str(test_n) + '.txt').read() == open('./Tests/TESToutput_' + str(test_n) + '.txt').read():
        print("OK " + str(test_n))
    else:
        print("BLYA")
        quit()

    os.remove('./Tests/TESTmyoutput_' + str(test_n) + '.txt')

print("Errors not found.\n" + str(test_n) + " tests passed.")
