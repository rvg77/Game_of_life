import random


def get(x):
    if x == 0:
        return '.'
    elif x == 1:
        return '#'
    elif x == 2:
        return 'F'
    elif x == 3:
        return 'C'


tests_n = 100

for t in range(tests_n):
    n = random.randint(1, 10)
    h = random.randint(1, 30)
    w = random.randint(1, 30)
    test = str(n) + '\n' + str(h) + ' ' + str(w)
    for i in range(h):
        s = ''.join(random.choices(['.', '#', 'F', 'C'], k=w))
        test += '\n' + s
    file = open('./Tests/TESTinput_' + str(t) + '.txt', 'w')
    file.write(test)
    file.close()
