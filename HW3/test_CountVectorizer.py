from HW_Class_1 import CountVectorizer


def test_empty():
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform([])
    assert vectorizer.get_feature_names() == [] and count_matrix == []


def test_only_string():
    corpus = ["Crock Pot Pasta Never boil pasta again"]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    vectors = [[1, 1, 2, 1, 1, 1]]
    feature_names = ["crock", "pot", "pasta", "never", "boil", "again"]
    assert vectorizer.get_feature_names() == feature_names and count_matrix == vectors


def test_instance_from_task():
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    vectors = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    feature_names = [
        "crock",
        "pot",
        "pasta",
        "never",
        "boil",
        "again",
        "pomodoro",
        "fresh",
        "ingredients",
        "parmesan",
        "to",
        "taste",
    ]
    assert vectorizer.get_feature_names() == feature_names and count_matrix == vectors

