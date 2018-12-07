import Modeling_lib
import Parse_input
import os

tests = 100
for test_n in range(tests):
    file = open('./sys_tests/TESTinput_' + str(test_n) + '.txt')
    lines = file.read().split('\n')
    file.close()

    n, h, w, ocean = Parse_input.get_inf(lines)

    first_gen = Modeling_lib.Generation(h, w, False)

    first_gen.set_ocean(ocean)

    life = Modeling_lib.Life(first_gen)

    file = open('./sys_tests/TESTmyoutput_' + str(test_n) + '.txt', 'w')
    file.write(str(life.get_generation(n)))
    file.close()

    if open('./sys_tests/TESTmyoutput_' + str(test_n) + '.txt').read() == open('./sys_tests/TESToutput_'
                                                                           + str(test_n) + '.txt').read():
        print("OK " + str(test_n))
    else:
        print("BLYA")
        quit()

    os.remove('./sys_tests/TESTmyoutput_' + str(test_n) + '.txt')

print("Errors not found.\n" + str(test_n) + " tests passed.")
