import pandas as pd

userMeans = pd.read_csv('csvs/userMeanRatings.csv')
userMovie = pd.read_csv('csvs/userMovieMatrix.csv')

meanRatings = list(userMeans['meanRating'])

movieIds = [str(i) for i in range(3953)]

userCorrelation = [ [0 for i in range(6041)] for j in range(6041) ]

#'''
'''
    find similarity between 2 users i and j based on their ratings for movie k
'''
for i in range(1,6041):   #6041):
    for j in range(1,6041):   #6041):
        corr_ij = 0.0
        numer = 0.0
        denom = 0.0
        denom_t1 = 0.0
        denom_t2 = 0.0
        if i < j:
            iMean = userMeans['meanRating'][i-1]
            jMean = userMeans['meanRating'][j-1]
            for k in movieIds:
                iRate = userMovie[k][i]
                jRate = userMovie[k][j]
                if iRate != 0 and jRate != 0:
                    numer += (iRate-iMean)*(jRate-jMean)
                    denom_t1 += (iRate-iMean)**2
                    denom_t2 += (jRate-jMean)**2
            denom = (denom_t1*denom_t2*1.0)**0.5
            if denom == 0:
                denom = 1
            corr_ij = numer / denom
            userCorrelation[i][j] = corr_ij
            userCorrelation[j][i] = corr_ij
            print(i,j, corr_ij)

#'''

#print(userCorrelation[1])

df = pd.DataFrame(userCorrelation)

df.to_csv('csvs/pearsonCorrelationMatrix.csv')
