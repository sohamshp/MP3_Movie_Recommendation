import pandas as pd
import datetime

file = open('ml-1m/ratings.dat')

userId = []
movieId = []
rating = []
timestamp = []

for i in file:
    i = i.splitlines()
    info = i[0].split('::')
    userId.append(info[0])
    movieId.append(info[1])
    rating.append(info[2])
    timestamp.append(info[3])

ratings = pd.DataFrame()

ratings['userId'] = userId
ratings['movieId'] = movieId
ratings['rating'] = rating
ratings['timestamp'] = timestamp

#print(ratings)

ratings.set_index(['userId','movieId'])

#ratings.to_csv('ml-1m/ratings.csv')
ratings.to_pickle('pickles/ratings.pickle')
