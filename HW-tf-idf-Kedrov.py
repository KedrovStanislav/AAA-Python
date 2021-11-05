from math import log


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


class TfidfTransformer:
    @staticmethod
    def tf_transform1(cnt_m):
        res = []
        for vec in cnt_m:
            res.append([frec / sum(vec) for frec in vec])
        return res

    @staticmethod
    def idf_transform1(cnt_m):
        cnt_doc = len(cnt_m)
        doc_w = [0] * len(cnt_m[0])
        for vec in cnt_m:
            for i in range(len(vec)):
                if vec[i] > 0:
                    doc_w[i] += 1
        return [log((cnt_doc + 1) / (x + 1)) + 1 for x in doc_w]

    @staticmethod
    def fit_transform(cnt_m):
        idf = TfidfTransformer.idf_transform1(cnt_m)
        tf = TfidfTransformer.tf_transform1(cnt_m)
        res = []
        for tf_i in tf:
            res.append([t_i_j * idf_j for t_i_j, idf_j in zip(tf_i, idf)])
        return res


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()

    def fit_transform(self, corpus):
        vectorizer = CountVectorizer()
        cnt_m = super().fit_transform(corpus)
        return TfidfTransformer.fit_transform(cnt_m)

