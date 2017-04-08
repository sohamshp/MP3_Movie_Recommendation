import sqlite3 as sql
import pandas as pd
from datetime import date
import numpy as np

conn = sql.connect('db.sqlite3')

c = conn.cursor()

d = date.today()

### Adding users
'''
file = pd.read_csv('../res/small/user_demo.csv')

userId = list(file['userId'])
gender = list(file['userGender'])
age = list(file['userAge'])
age_group = list(file['userAgeParsed'])
occupation = list(file['userJobParsed'])

length = len(gender)

insertions = []

for i in range(length):
    row = (
        int(i),
        int(userId[i]),
        "John", "Doe",
        gender[i],
        d, int(age[i]),
        age_group[i],
        occupation[i],
        "USA"
    )
    insertions.append(row)

c.executemany("INSERT INTO movie_users VALUES (?,?,?,?,?,?,?,?,?,?)", insertions[100:])

conn.commit()
'''

### Adding movies
'''

file = pd.read_pickle('../res/small/movies2.pickle')

movieId = list(file['movieId'])
title = list(file['movieTitle'])
year = list(file['movieYear'])
genre = list(file['movieGenre'])

length = len(title)

insertions = []

for i in range(10,length):
    row = (
        int(i),
        int(movieId[i]),
        title[i],
        int(year[i]),
        genre[i],
        ""
    )
    insertions.append(row)

c.executemany("INSERT INTO movie_movieinfo VALUES (?,?,?,?,?,?)", insertions)
conn.commit()
'''


### Adding Ratings
'''

file = pd.read_csv('../res/small/ratings.csv')

u_id = list(file['userId'])
m_id = list(file['movieId'])
rate = list(file['rating'])

length = len(u_id)

insertions = []

for i in range(length):
    row = (
        int(i),
        int(u_id[i]),
        int(m_id[i]),
        int(rate[i])
    )
    print(row)
    insertions.append(row)

c.executemany("INSERT INTO movie_ratings2 VALUES (?,?,?,?)", insertions)

conn.commit()

'''

### Adding predicted ratings
'''

file = pd.read_csv('../res/small/model_2.csv')

matrix = file.as_matrix()

insertions = []

i=0
for u in range(500):
    for m in range(3884):
        row = (
            i,
            int(u),
            int(m),
            float(matrix[u][m])
        )
        insertions.append(row)
        i += 1

c.executemany("INSERT INTO movie_predictionmodel VALUES (?,?,?,?)", insertions)

conn.commit()

'''

### Adding stored ratings
'''

file = pd.read_csv('../res/small/userMovieMat.csv')

matrix = file.as_matrix()

insertions = []

i=0
for u in range(500):
    for m in range(3884):
        row = (
            i,
            int(u),
            int(m),
            int(matrix[u][m])
        )
        insertions.append(row)
        i += 1

c.executemany("INSERT INTO movie_ummat VALUES (?,?,?,?)", insertions)

conn.commit()

'''

### Adding gender avgs
'''

dir = '../res/small/avgs/'

genders = ['M', 'F']

insertions = []
pk=0
for i in range(2):
    file = pd.read_csv(dir+'genderAvg'+str(i)+'.csv')
    print(len(file['0']))
    for j in range(len(file['0'])):
        row = (
            pk,
            i,
            genders[i],
            j,
            int(file['0'][j]),
            int(file['1'][j]),
            int(file['2'][j]),
            int(file['3'][j]),
            int(file['4'][j]),
            float(file['5'][j])
        )
        pk += 1
        insertions.append(row)


c.executemany("INSERT INTO movie_genderavg VALUES (?,?,?,?,?,?,?,?,?,?)", insertions)

conn.commit()

'''


### Adding Age avgs
'''

dir = '../res/small/avgs/'

ages = ['Under 18', '18-24', '25-34', '35-44', '45-49', '50-55', '56+']
agesVal = [1, 18, 25, 35, 45, 50, 56]

insertions = []
pk=0
for i in range(7):
    file = pd.read_csv(dir+'ageAvg'+str(i)+'.csv')
    print(len(file['0']))
    for j in range(len(file['0'])):
        row = (
            pk,
            i,
            agesVal[i],
            ages[i],
            j,
            int(file['0'][j]),
            int(file['1'][j]),
            int(file['2'][j]),
            int(file['3'][j]),
            int(file['4'][j]),
            float(file['5'][j])
        )
        pk += 1
        #print(row)
        insertions.append(row)



c.executemany("INSERT INTO movie_ageavg VALUES (?,?,?,?,?,?,?,?,?,?,?)", insertions)

conn.commit()

'''


#for i in c.execute("SELECT count(*) FROM movie_ageavg"):
#    print(i)

c.close()
conn.close()