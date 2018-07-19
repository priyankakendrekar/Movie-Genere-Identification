import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score, f1_score
import sys
import os
sys.stdout = open('logutils', 'w')
my_tags = ['animation', 'others']

def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(my_tags))
    target_names = my_tags
    plt.xticks(tick_marks, target_names, rotation=45)
    plt.yticks(tick_marks, target_names)
    # plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def evaluate_prediction(predictions, target, title="Confusion matrix"):
    #print('accuracy %s' % accuracy_score(target, predictions))
    #print('precision %s' % precision_score(target, predictions,pos_label='Animation'))
    #print('recall %s' % recall_score(target, predictions,pos_label='Animation'))
    #print('f-measure %s' % f1_score(target, predictions,pos_label='Animation'))

    print('accuracy %s' % accuracy_score(target, predictions))
    print('precision %s' % precision_score(target, predictions, average=None ))
    print('recall %s' % recall_score(target, predictions, average=None ))
    print('f-measure %s' % f1_score(target, predictions, average=None ))

    #cm = confusion_matrix(target, predictions)
    #print('confusion matrix\n %s' % cm)
    #print('(row=expected, col=predicted)')

    #cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    #plt.figure()
    #plot_confusion_matrix(cm_normalized, title + ' Normalized')
    #plt.show()


def predict(vectorizer, classifier, testdata):
    #Transform documents to document-term matrix.
    #test_data_features = vectorizer.transform(testdata['plot'])
    testplot = ["things seem change much wabasha county max john still fighting years grandpa still drinks smokes chases women nobody able catch fabled catfish hunter gigantic catfish actually smiles fishermen try snare six months ago john married new girl town ariel people begin suspect max might missing something similar life joy max claims left life fishing might change new owner bait shop"]
    test_data_features = vectorizer.transform(testplot)
    #Predict the class labels for the provided data
    predictions_genre = classifier.predict(test_data_features)
    print("Plot is : "+str(testplot))
    print("predicted genre: " +str(predictions_genre))
    #target_genre_truevalue = testdata['tags']
    #print("data_features " +str(test_data_features)+ " predictions: " +str(predictions_genre)+ " target " +str(target_genre_truevalue))	
    #evaluate_prediction(predictions_genre, target_genre_truevalue)
 

def getTags(genre, train):
    tagVector = []
    for tag in train['Genre1']:
        if tag == genre:
            tagVector.append(genre)
        else:
            tagVector.append('other')

    return tagVector

def getTagsArray(genreList, train):
    tagVector = []
    for tag in train['Genre1']:
        if tag == genreList[0]:
            tagVector.append(genreList[0])
        elif tag == genreList[1]:
              tagVector.append(genreList[1])
        else:
            tagVector.append('other')

    return tagVector	


		 
