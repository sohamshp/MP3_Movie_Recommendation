import pandas as pd

userMeans = pd.read_csv('csvs/userMeanRatings.csv')
userMovie = pd.read_csv('csvs/userMovieMatrix.csv')

meanRatings = list(userMeans['meanRating'])

squareRatings = list(userMeans['squareRating'])

movieIds = [str(i) for i in range(3953)]

userCorrelation = [ [0 for i in range(6041)] for j in range(6041) ]

#'''
'''

'''
for i in range(1, 6041):  # 6041):
    for k in range(1, 6041):  # 6041):
        corr_ik = 0.0
        for j in movieIds:
            if i < k:
                iRate = userMovie[j][i]
                kRate = userMovie[j][k]
                if iRate != 0 and kRate != 0:
                    corr_ik += (iRate*kRate)
                    corr_ik /= (squareRatings[i-1]*1.0)**0.5
                    corr_ik /= (squareRatings[k-1]*1.0)**0.5
                    #print(corr_ik)
        userCorrelation[i][k] = corr_ik
        userCorrelation[k][i] = corr_ik
        print(i,k, corr_ik)

#'''

print(userCorrelation[1])

df = pd.DataFrame(userCorrelation)

df.to_csv('csvs/vectorCosCorrelation.csv')
