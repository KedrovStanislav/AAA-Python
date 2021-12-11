import abc


class ComputerColor:
    @classmethod
    @abc.abstractmethod
    def __repr__(cls):
        pass

    @classmethod
    @abc.abstractmethod
    def __mul__(cls):
        pass

    @classmethod
    @abc.abstractmethod
    def __rmul__(cls):
        pass


class Color(ComputerColor):
    START = "\033[1;38;2"
    END = "\033[0"
    MOD = "m"

    def __init__(self, red, green, blue):
        self.r = min(red, 255)
        self.g = min(green, 255)
        self.b = min(blue, 255)

    def __repr__(self):
        return f"{self.START};{self.r};{self.g};{self.b}{self.MOD}●{self.END}{self.MOD}"

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __hash__(self):
        return self.r * 1000000 + self.g * 1000 + self.b

    @staticmethod
    def change_contr(part_of_color, c):
        cl = -256 * (1 - c)
        f = 259 * (cl + 255) / 255 / (259 - cl)
        return int(f * (part_of_color - 128) + 128)

    def __mul__(self, c):
        return Color(
            Color.change_contr(self.r, c),
            Color.change_contr(self.g, c),
            Color.change_contr(self.b, c),
        )

    __rmul__ = __mul__


class HSLColor(ComputerColor):
    START = "\033[1;38;2"
    END = "\033[0"
    MOD = "m"

    def __init__(self, p1, p2, p3):
        self.r = 0
        self.g = 0
        self.b = 0

    def __repr__(self):
        return f"{self.START};{self.r};{self.g};{self.b}{self.MOD}●{self.END}{self.MOD}"

    def __mul__(self, c):
        return Color(
            Color.change_contr(self.r, c),
            Color.change_contr(self.g, c),
            Color.change_contr(self.b, c),
        )

    __rmul__ = __mul__


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]

    for row in a_matrix:
        print("".join(str(ptr) for ptr in row))


print()
# Task 1
red = Color(255, 0, 0)
print(red)

print()
# Task 2
red = Color(255, 0, 0)
green = Color(0, 255, 0)
print(red == green)
print(red == Color(255, 0, 0))


print()
# Task 3
red = Color(255, 0, 0)
green = Color(0, 255, 0)
print(red + green)


print()
# Task 4
orange1 = Color(255, 165, 0)
red = Color(255, 0, 0)
green = Color(0, 255, 0)
orange2 = Color(255, 165, 0)
color_list = [orange1, red, green, orange2]
print(set(color_list))


print()
# Task 5
red = Color(255, 0, 0)
print(red)
print(0.5 * red)

print()
# Task 6
c2 = HSLColor(0, 255, 0)
print_a(c2)