import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC

count_vect = CountVectorizer()
tfidf_transformer = TfidfTransformer()

def classify(text):
    try:
        tweets=pd.read_csv("tweet_category.csv")
        X_train,  y_train = tweets['content'],tweets['category']
        X_train_counts = count_vect.fit_transform(X_train)
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        clf =LinearSVC().fit(X_train_tfidf, y_train)
        return(clf.predict(count_vect.transform([text])))
    except:
        return ''
