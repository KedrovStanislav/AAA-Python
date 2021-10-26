class CountVectorizer:
    def __init__(self):
        self.__count_matrix = []
        self.__features = {}

    def fit_transform(self, strings: list) -> list:
        for string in strings:
            vect = [0] * len(self.__features)
            words = string.lower().split()
            for word in words:
                if word in self.__features:
                    vect[self.__features[word]] += 1
                else:
                    self.__features[word] = len(self.__features)
                    vect.append(1)
            self.__count_matrix.append(vect)

        for vect in self.__count_matrix:
            vect.extend([0] * (len(self.__features) - len(vect)))
        return self.__count_matrix

    def get_feature_names(self) -> list:
        return list(self.__features.keys())
