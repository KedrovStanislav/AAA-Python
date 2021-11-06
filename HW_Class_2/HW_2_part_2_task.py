import json


class ColorizeMixin:
    """ For Mixin for set color"""

    repr_color_code = 33


class Advert(ColorizeMixin):
    """Convert json (dict) to object for access by dot """

    def __init__(self, info: dict):
        self.price = 0
        for clause in info:
            if type(info[clause]) is dict:
                self.__dict__[clause] = Advert(info[clause])
            elif clause == "price" and info[clause] < 0:
                print("ValueError: must be >= 0")
            else:
                self.__dict__[clause] = info[clause]

    def __repr__(self):
        return f"\033[0;{self.repr_color_code};40m{self.title} | {self.price} ₽"


if __name__ == "__main__":
    iphone_ad = Advert({"title": "python", "price": 100})
    print(iphone_ad)

