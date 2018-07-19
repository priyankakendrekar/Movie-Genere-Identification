import requests
import json
import unicodecsv as csv
import pandas as pd
import sys
import os

movieCount = 0
# seedMovie = 120903
# maxCount = 500
# movieIndex = 0
movies = pd.read_csv('data/links1000.csv', converters={'imdbId': lambda x: str(x)})

# movieIdSuffix = movies['imdbId'][movieIndex]

fieldNames = ['imdbID', 'Title', 'Plot', 'Genre1', 'Genre2', 'Genre3']


def getNewDict(data):
    newDict = {}
    newDict["imdbID"] = data["imdbID"]
    newDict["Title"] = data["Title"]
    newDict["Plot"] = data["Plot"]

    genres = data["Genre"].split(',')

    i=1
    for genre in genres:
        newDict["Genre" + str(i)] = genre
        i=i+1

    for j in range(i,4):
        newDict["Genre" + str(j)] = ""
   
    print("getting new dict")
    return newDict


with open('omdbdata1.csv','wb') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldNames, extrasaction='ignore')
    csvwriter.writeheader()

    for movieIdSuffix in movies['imdbId']:
        url = "http://www.omdbapi.com/?i=tt"+str(movieIdSuffix)+"&fullplot=True&apikey=3b1740a3"
        print(" url "+url)
		
        try:
            #print("fetching3 "+movieIdSuffix+"http://www.omdbapi.com/?i=tt3896198&apikey=3b1740a3?plot=full&i=tt0" + str(movieIdSuffix))
            
            r = requests.get(url)
            #print(" r "+r)
            data = json.loads(r.text)
            #print(" data is "+data)
            response = data['Response']
            #print(" response is "+response)			
            if (response == "True"):
                plot = data['Plot']
                type = data['Type']
                genre = data['Genre']
                # language = data['Language']
                # country = data['Country']
                print(" Plot is "+plot)
                if (type == 'movie' and len(plot) > 50 and genre != 'N/A'):
                    movieCount += 1
                    print("Processing movie no : " + str(movieCount))
                    finalData = getNewDict(data)
                    csvwriter.writerow(finalData)
            else:
                print("response = false")			
            # movieIndex += 1
            # movieIdSuffix = movies['imdbId'][movieIndex]

        except Exception as e:
            print("exception! "+str(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            # movieIndex += 1
            # movieIdSuffix = movies['imdbId'][movieIndex]
            continue

print (movieIdSuffix)