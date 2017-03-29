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


for i in c.execute("SELECT count(*) FROM movie_ummat"):
    print(i)

c.close()
conn.close()