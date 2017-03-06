import pandas as pd

ratings = pd.read_pickle('pickles/ratings.pickle')
movieInfo = pd.read_pickle('pickles/movieInfo.pickle')

# movieId movieTitle movieGenre
movieIdSet = list(set(movieInfo['movieId']))
movieIdsSorted = [int(i) for i in movieIdSet]
movieIdsSorted = sorted(movieIdsSorted)
movieIdsSortedStr = [str(i) for i in movieIdsSorted]

# userId movieId rating  timestamp


#data = pd.DataFrame([], columns=movieIdsSortedStr)

userRating = [0 for i in range(3953)]
movieIds = [i for i in range(3953)]

#print(len(userRating), len(movieIds))

userMovieRatings = [ [0 for i in range(3953)] for j in range(6041) ]

print(len(userMovieRatings))
print(len(userMovieRatings[0]))

#for i in range(10):       #range(6041):
#    userMovieRatings.append(userRating)

'''
count = 0
for i in userMovieRatings:
    count += 1
    print(len(i))

print(count)
'''

userdb = list(ratings['userId'])
moviedb = list(ratings['movieId'])
ratedb = list(ratings['rating'])

length = len(userdb)

print(length)

for i in range(length):
    uId, mId, rt = int(userdb[i]), int(moviedb[i]), int(ratedb[i])
    userMovieRatings[uId][mId] = rt
#    print(userMovieRatings[uId][mId], rt)

#for i in range(len(indices)-1):
#    for j in range(indices[i],indices[i+1]):
#        print(j)

df = pd.DataFrame(userMovieRatings)

df.to_csv('csvs/yolo2.csv')