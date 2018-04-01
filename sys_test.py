import Modeling_lib
import Parse_input
import os

tests = 100
for test_n in range(tests):
    file = open('./Sys_tests/TESTinput_' + str(test_n) + '.txt')
    lines = file.read().split('\n')
    file.close()

    n, h, w, ocean = Parse_input.get_inf(lines)

    first_gen = Modeling_lib.Generation(h, w, False)

    first_gen.set_ocean(ocean)

    life = Modeling_lib.Life(first_gen)

    file = open('./Sys_tests/TESTmyoutput_' + str(test_n) + '.txt', 'w')
    file.write(life.get_generation(n).print_gen())
    file.close()

    if open('./Sys_tests/TESTmyoutput_' + str(test_n) + '.txt').read() == open('./Sys_tests/TESToutput_'
                                                                           + str(test_n) + '.txt').read():
        print("OK " + str(test_n))
    else:
        print("BLYA")
        quit()

    os.remove('./Sys_tests/TESTmyoutput_' + str(test_n) + '.txt')

print("Errors not found.\n" + str(test_n) + " tests passed.")
