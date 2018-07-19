import pandas as pd
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from utils import getTags
from utils import getTagsArray

def plotToWords(raw_plot):
    plot = BeautifulSoup(raw_plot, "lxml")
    letters_only = re.sub("[^a-zA-Z]", " ", plot.get_text())
    lower_case = letters_only.lower()
    words = lower_case.split()
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if not w in stops]
    return (" ".join(meaningful_words))

def preprocess(filename):
    train = pd.read_csv(filename)
    # counts = train.Genre1.value_counts()
    # counts.plot(kind='bar')
    # plt.show()
    # print counts

    num_plot = train["Plot"].size
    clean_train_plot = []

    for i in range(0, num_plot):
        if ((i + 1) % 100 == 0):
            k=i+1		
            #print ("Review " + str(k) + " of " + str(num_plot) + "\n" )
        clean_train_plot.append(plotToWords(train["Plot"][i]))
        #if (i<20) :
            #print("clean train plot "+str(i)+ " "+str(clean_train_plot[i]) )
			
    #tagVector = getTags('Animation', train)
    tagVector = getTagsArray(['Animation', 'Comedy'], train)
	#plot = getPlot('This story based on the best selling novel by Terry McMillan follows the lives of four African-American women as they try to deal with their very lives. Friendship becomes the strongest bond between these women as men, careers, and families take them in different directions. Often light-hearted this movie speaks about some of the problems and struggles the modern women face in todays world',train)
    #data = {'plot': clean_train_plot, 'tag': plot}
    data = {'plot': clean_train_plot, 'tags': tagVector}
    df = pd.DataFrame(data)
    #with pd.option_context('display.max_rows', 20):
        #print(df)

    return df