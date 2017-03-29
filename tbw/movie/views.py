from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.contrib.staticfiles.templatetags.staticfiles import static

import pandas as pd
import numpy as np
import operator as op

# Create your views here.
def index(request):
    context = {}
    return render(request, 'movie/index.html', context)

''' old searchres
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
'''
def searchres(request):
    strg = request.GET['key']
    divset=[]
    try:
        if strg != "":
            mov = MovieInfo.objects.filter(name__contains=strg)[0:5]
            for indx in mov:
                year_str = str(indx.year)
                name_str = indx.name
                div = "<div class=\'sres\'><div class=\'sres_des\'>"+ name_str +"<br><span class=\'sres_year\'>"+ year_str +"</span></div></div>"
                divset.append(div)
    except(KeyError, MovieInfo.DoesNotExist):
        return JsonResponse({"divset": [""]})
    else:
        print(divset)
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


def predict(request, u_id):
    u_id = int(u_id)
    p_rates = PredictionModel.objects.filter(userId=u_id).order_by('-rating')
    #for i in p_rates[:10]:
    #    print(i.userId, i.movieId, i.rating)
    #print(len(p_rates))
    rated = UMMat.objects.filter(userId=u_id).exclude(rating=0)
    ratedIds = []
    for i in rated:
        ratedIds.append(i.movieId)
    ratedIds = sorted(ratedIds)
    #print(ratedIds)
    p_rates = p_rates.exclude(movieId__in=ratedIds)
    #print(len(p_rates))
    #for i in p_rates[:10]:
    #    print(i.userId, i.movieId, i.rating)

    mset = []
    for i in p_rates[:20]:
        movinf = {}
        mov = MovieInfo.objects.get(m_id=i.movieId)
        mset.append(mov)
    return HttpResponse(mset)

def makeUnrated(request):
    file = pd.read_csv("C:/Users/shp/Desktop/Movie Recommendation system/res/small/userMovieMat.csv")
    arr = file.as_matrix()
    pri = 1
    for i in range(5): # 501
        userUnrated = np.nonzero(arr[i]==0)
        print(userUnrated[0])
        for j in userUnrated[0]:
            u = Unrated(user_id=i, movie_id=j)
            print(u, i, j)
            #u.save()
        '''
        for j in range(3953): # 3953
            if arr[i][j] == 0:
                try:
                    #r = Unrated.objects.get(pk=pri)
                    #r.delete()
                    #print(i,j,r, 'delete')
                    pri+=1
                except:
                    u = Unrated(user_id=i, movie_id=j)
                    #print(u,i,j)
                    u.save()
                    pri+=1
        '''
    return HttpResponse('hala')


def getImdb(request):
    file = pd.read_pickle("C:/Users/shp/Desktop/Movie Recommendation system/res/small/movies3.pickle")

    mIds = list(file['movieId'])
    imdbL = list(file['imdbLink'])

    linked = {}
    for i in range(len(mIds)):
        linked[int(mIds[i])] = 'tt'+str(imdbL[i])

    for i in range(len(mIds)):
        try:
            mov = MovieInfo.objects.get(pk=i)
            print(mov.m_id)
            idd = mov.m_id
            print(idd)
            ss = linked[idd]
            print(ss)
            mov.imdb = ss
            #mov.save()
        except:
            print('noooooo')
    return HttpResponse('wooo')
