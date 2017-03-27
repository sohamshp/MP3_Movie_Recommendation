import pandas as pd

movies = pd.read_pickle('pickles/movieInfo.pickle')

movieIds = movies['movieId']
mov = movies['movieTitle']
genres = movies['movieGenre']

movieTitle = []
movieYear = []

for i in range(len(mov)):
    title = mov[i][:-7]
    year = int(mov[i][-5:-1])
    movieTitle.append(title)
    movieYear.append(year)


newMov = pd.DataFrame()

newMov['movieId'] = movieIds
newMov['movieTitle'] = movieTitle
newMov['movieYear'] = movieYear
newMov['movieGenre'] = genres

newMov.to_csv('small/movies2.csv')
newMov.to_pickle('small/movies2.pickle')