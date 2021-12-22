import click
import random


class Pizza:
    def print_recipe(self):
        print(
            "- "
            + list(self.recipe.keys())[0]
            + ": "
            + ", ".join(list(self.recipe.values())[0])
        )

    def dict(self):
        print(self.recipe)


class Margherita(Pizza):
    def __init__(self, size="L"):
        self.size = size
        self.recipe = {"Margherita": ["tomato sauce", "mozzarella", "tomatoes"]}


class Pepperoni(Pizza):
    def __init__(self, size="L"):
        self.size = size
        self.recipe = {"Pepperoni": ["tomato sauce", "mozzarella", "pepperoni"]}


class Hawaiian(Pizza):
    def __init__(self, size="L"):
        self.size = size
        self.recipe = {
            "Hawaiian": ["tomato sauce", "mozzarella", "chicken", "pineapples"]
        }


def log(function):
    def wrapper():
        function()
        time = random.randint(1, 10)
        print(f"{function.__name__} - {time}c!")

    return wrapper


@log
def bake():
    """Готовит пиццу"""
    pass


@log
def deliver_to_you():
    """Доставляет пиццу"""
    pass


@log
def pickup():
    """Самовывоз"""
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    bake()
    if delivery:
        deliver_to_you()
    else:
        pickup()


@cli.command()
def menu():
    """Выводит меню"""
    Margherita().print_recipe()
    Pepperoni().print_recipe()
    Hawaiian().print_recipe()


if __name__ == "__main__":
    cli()
