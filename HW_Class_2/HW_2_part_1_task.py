class Advert:
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
