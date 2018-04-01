import Modeling_lib
import pytest


class TestGeneration:
    def test_construction(self):
        with pytest.raises(TypeError):
            Modeling_lib.Generation('string', 1, False)
        with pytest.raises(TypeError):
            Modeling_lib.Generation(1, 'string', False)
        with pytest.raises(TypeError):
            Modeling_lib.Generation(1, 1, 'string')
        with pytest.raises(RuntimeError):
            Modeling_lib.Generation(-1, 1, True)
        with pytest.raises(RuntimeError):
            Modeling_lib.Generation(1, -1, False)
        gen = Modeling_lib.Generation(10, 10, True)
        assert (len(gen.ocean) == 10)
        for i in range(len(gen.ocean)):
            assert (len(gen.ocean[i]) == 10)

    def test_setter(self):
        gen = Modeling_lib.Generation(1, 1, True)
        with pytest.raises(TypeError):
            gen.set_ocean('string')
        with pytest.raises(RuntimeError):
            gen.set_ocean([])
        with pytest.raises(RuntimeError):
            gen.set_ocean([[]])
        ocean = [[Modeling_lib.Fish()]]
        gen.set_ocean(ocean)
        assert (gen.ocean == ocean)

    pass


class TestLife:

    def test_construction(self):
        with pytest.raises(RuntimeError):
            Modeling_lib.Life(None)
        gen = Modeling_lib.Generation(1, 1, True)
        ocean = [[Modeling_lib.Fish()]]
        gen.set_ocean(ocean)
        life = Modeling_lib.Life(gen)
        assert life.generations[0] == gen

    def test_getter(self):
        gen = Modeling_lib.Generation(1, 1, True)
        ocean = [[Modeling_lib.Fish()]]
        gen.set_ocean(ocean)
        life = Modeling_lib.Life(gen)

        with pytest.raises(TypeError):
            life.get_generation(False)
        with pytest.raises(RuntimeError):
            life.get_generation(-1)
        life.next_generation()
        assert life.generations[-1].ocean[0][0].name == '.'

    pass
