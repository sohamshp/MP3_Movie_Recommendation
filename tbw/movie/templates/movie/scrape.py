import urllib
import json

ut = urllib.urlopen("http://www.omdbapi.com/?i=tt3315342").read()
rt = json.loads(ut)
print(rt["Title"])
urllib.urlretrieve(rt["Poster"],"localimg.jpg")