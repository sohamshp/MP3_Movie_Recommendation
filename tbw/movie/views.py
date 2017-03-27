from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Movies, Ratings, Users, MovieInfo
from django.contrib.staticfiles.templatetags.staticfiles import static

import pandas as pd

# Create your views here.
def index(request):
    context = {}
    return render(request, 'movie/index.html', context)

def searchres(request):
    str = request.GET['key']
    divset=[]
    try:
        if str != "":
            mov = Movies.objects.filter(name__contains=str)[0:5]

            for indx in mov:
                div = "<div class=\'sres\'><img src=\'"+ static("movie/images/"+indx.poster) +"\' class=\'search_poster\'/><div class=\'sres_des\'>"+ indx.name +"<br><span class=\'sres_year\'>"+ indx.year +"</span></div></div>"
                divset.append(div)

    except(KeyError, Movies.DoesNotExist):
        return JsonResponse({"divset": [""]})
    else:
        return JsonResponse({"divset": divset})


def addRatings(request):
    #file = pd.read_csv('../../res/small/ratings.csv')
    file = pd.read_csv("C:/Users/shp/Desktop/Movie Recommendation system/res/small/ratings.csv")
    u_id = list(file['userId'])
    m_id = list(file['movieId'])
    rate = list(file['rating'])
    length = len(u_id)
    # 65507
    '''
    for i in range(65500,length):
        try:
            r = Ratings.objects.get(pk=i)
            print(r, i, "done")
        except:
            u = Users.objects.get(u_id=u_id[i])
            m = MovieInfo.objects.get(m_id=m_id[i])
            row = Ratings(user=u, movie=m, rating=int(rate[i]))
            print(row, i)
            row.save()
    '''
    return HttpResponse("kjsdagfkalshf")