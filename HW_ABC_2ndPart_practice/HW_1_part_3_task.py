import random
import abc


class AnimeMon:
    @property
    @abc.abstractmethod
    def exp(cls):
        pass

    @exp.setter
    @abc.abstractmethod
    def exp(self, val):
        pass

    @classmethod
    @abc.abstractmethod
    def inc_exp(cls):
        pass


class Pokemon(AnimeMon):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self._exp = 0

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value

    def inc_exp(self, step_size):
        self.exp += step_size


class Digimon(AnimeMon):
    def __init__(self, name):
        self.name = name
        self._exp = 0

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value

    def inc_exp(self, value: int):
        self.exp += value * 8


def train(pokemon: Pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for _ in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


if __name__ == "__main__":
    bulbasaur = Pokemon(name="Bulbasaur", poketype="grass")
    train(bulbasaur)
    print(bulbasaur.exp)
    print()
    agumon = Digimon(name="Agumon")
    train(agumon)
    print(agumon.exp)                

