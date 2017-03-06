import pandas as pd

ratings = pd.read_pickle('pickles/ratings.pickle')

#users = list(set(ratings['userId']))

#print(len(users))

userRatings = [0 for i in range(6041)]
userRateCounts = [0 for j in range(6041)]

userSquareRatings = [0 for i in range(6041)]

# userId movieId rating  timestamp

for i in range(len(ratings['userId'])):
    userIndex = int(ratings['userId'][i])
    userRateCounts[userIndex] += 1
    userRatings[userIndex] += int(ratings['rating'][userIndex])
    userSquareRatings[userIndex] += int(ratings['rating'][userIndex])**2

print(len(userRatings))
print(len(userRateCounts))

userMeanRatings = [0 for i in range(6041)]

for i in range(1,6041):
    userMeanRatings[i] = userRatings[i]/userRateCounts[i]

print(len(userMeanRatings))
print(userMeanRatings)

userIds = [i for i in range(6041)]

df = pd.DataFrame()

df['userId'] = userIds[1:]
df['meanRating'] = userMeanRatings[1:]
df['squareRating'] = userSquareRatings[1:]

df.to_pickle('pickles/userMeanRatings.pickle')
df.to_csv('csvs/userMeanRatings.csv')
