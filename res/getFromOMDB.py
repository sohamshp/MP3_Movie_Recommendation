import requests
import pandas as pd
import json

movieInfo = pd.read_pickle('pickles/movieInfo.pickle')

#index = 2
#print(movieInfo['movieTitle'][index])
#searchString = 'http://www.omdbapi.com/?t='
#title = movieInfo['movieTitle'][index][:-7]
#title = title.split(' ')
#title = '+'.join(title)
#print(title)
#searchString += title
#print(searchString)
#r = requests.get(searchString)
#print(r.json())
#data = r.json()

api = 'http://www.omdbapi.com/?t='
movieTitles = list(movieInfo['movieTitle'])
mul = 14
rows = 10
imdbInfo = pd.DataFrame()


for mul in range(43, 390):
    print(0+mul*rows, 10+mul*rows)
    imdbInfo = pd.DataFrame()
    for index in range(0+mul*rows, 10+mul*rows):  #len(movieTitles)):
        if index == len(movieTitles):
            break
        search = ''
        title = movieTitles[index][:-7].split(' ')
        title = '+'.join(title)
        search = api + title
        r = requests.get(search)
        j = r.json()
        print(j)
        for key in j.keys():
            imdbInfo.loc[index, key] = j[key]
    imdbInfo.to_csv('excels/imdbInfo'+str(mul)+'.csv')

'''
df = pd.DataFrame()
for key in data.keys():
    df.loc[0,key] = data[key]
'''

'''
runtime = []
country = []
year = []
poster = []
metascore = []
imdbID = []
imdbVotes = []
language = []
awards = []
type = []
plot = []
rated = []
director = []
writer = []
actors = []
imdbRating = []
released = []
response = []
genre = []
title = []
'''