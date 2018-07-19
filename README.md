# Movie-Genre-Identification
Movie genre classification by movie plot.
## Aim: 
Given a plot story of movie (more than 50 characters), identify its Genre (Total 19 Genres)
## Dataset: 
I used a web api to build my data set. The name of the web api that I used is OMDB api. This api is capable of returning all the the data about a movie/series in a json/xml format given the imdb id of the movie. I started with a seed title ID and kept on increamenting it until I reached the target number of movies.
The api returns a lot of data about the movies/series, I just selected some features out of the whole set which are as follows :
1 Movie ID
2 Plot : Full (choices were Short or Full)
3 Genre
There are movies which are associated with more than one Genre and there can be as much as 4 Genres. I selected the first one as the main Genre and based my findings on that.
Here are some numbers for my data:
* Number of titles collected : 4456
* Genres Collected : 19


|               |               |       |
| ------------- |:-------------:| -----:|
| Comedy      | Action        | Drama |
| Animation   | Documentary   | Adventure |
| Biography   | Horror        | Fantasy |
| Mystery     | Romance       | Sci-Fi |
| Family      | Thriller      | Short |
| War         | Musical       | Western |
| Crime        |              |       | 

## Description: 
Text preprocessing is done to remove words unrelated to Genre. 
Classifiers are trained on word frequency vector in order to identify Genre 
Languages/Tools used: Python, Scikit-Learn (Machine Learning toolkit in Python), NLTK .
Keywords: Text Mining, Bag of words vector space, TF-IDF, KNN and SVM classifier.

Data Preprocessing
==================

After all the data was collected, some preprocessing was done on it:

* Any/all use of HTML tags were removed using BeautifulSoup library.
* Punctuation, Numbers and special characters were removed using a regex find and replace.
* All the stop words which were irrelevant to the context were removed using stopwords from Natural Language Toolkit (NLTK)


Data Mining
===========

I used a 90-10 train-test split ratio for test and train sets respectively.
All the preprocessed plot strings were then converted to bag of
Words(bow) form and various Machine learning methods were applied.

Results
===========
The best accuracy was achieved by using SVM with tfidf and an accuracy of **75.8** was achieved.





