import pandas as pd
import xlrd
import xlwt


#genome_scores = pd.read_csv('C:/users/shp/Desktop/Movie Recommendation system/data_20M/genome_scores.csv')
#genome_tags = pd.read_csv('C:/users/shp/Desktop/Movie Recommendation system/data_20M/genome_tags.csv')
#rating = pd.read_csv('C:/users/shp/Desktop/Movie Recommendation system/data_20M/rating.csv')
#tag = pd.read_csv('C:/users/shp/Desktop/Movie Recommendation system/data_20M/tag.csv')

link = pd.read_csv('C:/users/shp/Desktop/Movie Recommendation system/data_20M/link.csv')
movie = pd.read_csv('C:/users/shp/Desktop/Movie Recommendation system/data_20M/movie.csv')

#print(link.head(1))
#print(movie.head(1))

joined = movie.set_index('movieId').join(link.set_index('movieId'))

#print(joined)

joined.to_csv('C:/users/shp/Desktop/Movie Recommendation system/joined.csv')


#joined = pd.read_pickle('joined.pickle')

#print(joined)