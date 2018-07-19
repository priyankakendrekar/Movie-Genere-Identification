from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from utils import predict
import sys
import os
import numpy as np
sys.stdout = open('logknn', 'w')

from preprocess import preprocess

data_features = preprocess("../omdbdata1.csv")

train_data, test_data = train_test_split(data_features, test_size=0.1, random_state=100)

vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=3000)
train_data_features = vectorizer.fit_transform(train_data['plot'])
#print("Vectorizer : " +str(vectorizer.vocabulary_ ))
train_data_features = train_data_features.toarray()
#np.set_printoptions(threshold=np.inf)
#print("tarin data features\n{}".format(train_data_features))
#print("traindatafeartures: " +str(type(train_data_features)))
#print("train data features: " +str(train_data_features[0]))
#http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
knn_naive_dv = KNeighborsClassifier(n_neighbors=3, n_jobs=1, algorithm='brute', metric='cosine')
#Fit the model using train_data_features as training data and train data tags as target values
knn_naive_dv = knn_naive_dv.fit(train_data_features, train_data['tags'])

predict(vectorizer, knn_naive_dv, test_data)