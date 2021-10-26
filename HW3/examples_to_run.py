from HW_Class_1 import CountVectorizer

if __name__ == "__main__":
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform([]))
    print(vectorizer.get_feature_names())

    print()
    corpus = ["Crock Pot Pasta Never boil pasta again"]
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names())

    print()
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names())