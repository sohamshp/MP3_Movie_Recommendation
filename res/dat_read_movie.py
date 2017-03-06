import pandas as pd

file = open('ml-1m/movies.dat')

movieId = []
movieTitle = []
movieGenre = []

for i in file:
    i = i.splitlines()
    info = i[0].split('::')
    movieId.append(info[0])
    movieTitle.append(info[1])
    movieGenre.append(info[2])

movieInfo = pd.DataFrame()

movieInfo['movieId'] = movieId
movieInfo['movieTitle'] = movieTitle
movieInfo['movieGenre'] = movieGenre

movieInfo.set_index('movieId')

#print(movieInfo)

#movieInfo.to_csv('ml-1m/movieInfo.csv')
movieInfo.to_pickle('pickles/movieInfo.pickle')
