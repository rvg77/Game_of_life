class Cell:
    pass


class Fish(Cell):
    name = 'F'

    @staticmethod
    def update(neighbours):
        cnt = neighbours.count(Fish.name)
        if cnt == 2 or cnt == 3:
            return Fish()
        else:
            return Void()


class Crayfish(Cell):
    name = 'C'

    @staticmethod
    def update(neighbours):
        cnt = neighbours.count(Crayfish.name)
        if cnt == 2 or cnt == 3:
            return Crayfish()
        else:
            return Void()


class Rock(Cell):
    name = '#'

    @staticmethod
    def update(neighbours):
        return Rock()


class Void(Cell):
    name = '.'

    @staticmethod
    def update(neighbours):
        if neighbours.count(Fish.name) == 3:
            return Fish
        elif neighbours.count(Crayfish.name) == 3:
            return Crayfish
        else:
            return Void


class Generation:
    """Describes a generation in particular moment."""

    def __init__(self, h, w, is_thor):
        """Initializes a generation.

        h and w should be int(height and width of the ocean), is_thor should be bool.

        """

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

        self._width = w
        self._height = h
        self._is_thor = is_thor
        self._ocean = [[None] * w for i in range(h)]

    def set_ocean(self, ocean):
        """Sets ocean.

        Ocean should be a two-dimensional array.

        """

        if type(ocean) is not list:
            raise TypeError('type of ocean should be list')
        if len(ocean) != self._height:
            raise RuntimeError('Incorrect h')
        for i in range(self._height):
            if len(ocean[i]) != self._width:
                raise RuntimeError('Incorrect w')

        self._ocean = ocean

    def try_to_reach(self, xx, yy):
        if self._is_thor:
            return self._ocean[xx % self._height][yy % self._width]
        else:
            if xx < 0 or xx >= self._height:
                return None
            if yy < 0 or yy >= self._width:
                return None
            return self._ocean[xx][yy]

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
        return self._ocean[x][y].update(neighbours)

    def next(self):
        """Returns next generation after self."""

        new_gen = Generation(self._height, self._width, self._is_thor)
        for i in range(self._height):
            for j in range(self._width):
                new_gen._ocean[i][j] = self.update(i, j)
        return new_gen

    def __str__(self, *args, **kwargs):
        """Returns graphical view of generation in string format."""

        s = ''
        for line in self._ocean:
            for i in line:
                s += i.name
            s += '\n'
        return s


class Life:
    """Descibes the history of the game from the beginning."""

    def __init__(self, gen):
        """Initialize self. gen should be an object of class Generation."""

        if not isinstance(gen, Generation):
                raise RuntimeError('gen should be an instance of Generation')

        self.generations = [gen]

    def next_generation(self):
        """Adds next generation to list of generations."""

        self.generations.append(self.generations[-1].next())

    def get_generation(self, n):
        """Calculates all generations up to the n (inclusevely) and returns the last.

        N should be type of int.

        """

        if type(n) is not int:
            raise TypeError('type of n should be int')
        if n < 0:
            raise RuntimeError('''n should be non-negative''')

        if len(self.generations) > n:
            return self.generations[n]

        while len(self.generations) <= n:
            self.next_generation()

        return self.generations[-1]
