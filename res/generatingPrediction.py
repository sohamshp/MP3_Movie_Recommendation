import pandas as pd

userMeans = pd.read_csv('csvs/userMeanRatings.csv')
userMovie = pd.read_csv('csvs/userMovieMatrix.csv')
# load user correlation matrix here as userCorr

meanRatings = list(userMeans['meanRating'])

movieIds = [str(i) for i in range(3953)]

'''
Current user: a
Current movie: j
'''

a = 27
j = 345

numUsers = len(meanRatings)

predicted = 0

if a <= numUsers:
    predicted = meanRatings[a-1]

numer = 0.0
denom = 0.0
for i in range(1,10):     #6041):
    numer += userMovie[str(j)][i] * userCorr[str(i)][a]
    denom += abs(userCorr[str(i)][a])

predicted += numer / denom

print(predicted)