
class Fish:
    name = 'F'

    @staticmethod
    def update(neighbours):
        cnt = neighbours.count(Fish.name)
        if cnt == 2 or cnt == 3:
            return Fish()
        else:
            return Void()

    pass


class Crayfish:
    name = 'C'

    @staticmethod
    def update(neighbours):
        cnt = neighbours.count(Crayfish.name)
        if cnt == 2 or cnt == 3:
            return Crayfish()
        else:
            return Void()

    pass


class Rock:
    name = '#'

    @staticmethod
    def update(neighbours):
        return Rock()

    pass


class Void:
    name = '.'

    @staticmethod
    def update(neighbours):
        if neighbours.count(Fish.name) == 3:
            return Fish
        elif neighbours.count(Crayfish.name) == 3:
            return Crayfish
        else:
            return Void

    pass


class Generation:
    def __init__(self, h, w, is_thor):
        if type(w) is not int:
            raise TypeError("type of w argument should be int")
        if w <= 0:
            raise RuntimeError('w should be positive')
        if type(h) is not int:
            raise TypeError("type of h argument should be int")
        if h <= 0:
            raise RuntimeError('h should be positive')
        if type(is_thor) is not bool:
            raise TypeError("type of num argument should be int")

        self.weight = w
        self.height = h
        self.is_thor = is_thor
        self.ocean = [[None] * w for i in range(h)]

    def set_ocean(self, ocean):
        if type(ocean) is not list:
            raise TypeError('type of ocean should be list')
        if len(ocean) != self.height:
            raise RuntimeError('Incorrect h')
        for i in range(self.height):
            if len(ocean[i]) != self.weight:
                raise RuntimeError('Incorrect w')

        self.ocean = ocean

    def try_to_reach(self, xx, yy):
        if self.is_thor:
            return self.ocean[xx % self.height][yy % self.weight]
        else:
            if xx < 0 or xx >= self.height:
                return None
            if yy < 0 or yy >= self.weight:
                return None
            return self.ocean[xx][yy]

    def get_neighbours(self, x, y):
        ans = list()

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                ans.append(self.try_to_reach(x + dx, y + dy))
        return ans

    def update(self, x, y):
        neighbours = [i.name for i in self.get_neighbours(x, y) if i is not None]
        return self.ocean[x][y].update(neighbours)

    def next(self):
        new_gen = Generation(self.height, self.weight, self.is_thor)
        for i in range(self.height):
            for j in range(self.weight):
                new_gen.ocean[i][j] = self.update(i, j)
        return new_gen

    def print_gen(self):
        s = ''
        for line in self.ocean:
            for i in line:
                s += i.name
            s += '\n'
        return s

    pass


class Life:
    def __init__(self, gen):
        if not isinstance(gen, Generation):
                raise RuntimeError('gen should be an instance of Generation')

        self.generations = [gen]

    def next_generation(self):
        self.generations.append(self.generations[-1].next())
        pass

    def get_generation(self, n):
        if type(n) is not int:
            raise TypeError('type of n should be int')
        if n < 0:
            raise RuntimeError('''n should be non-negative''')

        while len(self.generations) <= n:
            self.next_generation()

        return self.generations[-1]

    pass
