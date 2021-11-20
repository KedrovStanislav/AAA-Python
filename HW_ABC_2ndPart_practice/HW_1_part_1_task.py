import random


class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self.exp = 0

    def inc_exp(self, step_size):
        self.exp += step_size


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
