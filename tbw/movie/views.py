from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.contrib.staticfiles.templatetags.staticfiles import static
from django import forms
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.staticfiles.templatetags.staticfiles import static

from movie.forms import *

import pandas as pd
import numpy as np
import operator as op
from random import shuffle

# Create your views here.
# def index(request):
#    context = {}
#    return render(request, 'movie/index.html', context)

idList = []
rateList = []
loaded = False


class index(View):
    form_class = signinForm
    template_name = 'movie/index.html'
    imgURL = ''

    def get(self, request):
        form = self.form_class(None)

        if request.user.is_authenticated:
            usr = User.objects.filter(username=request.user.username)[0]
            prof = Profile.objects.filter(username=usr)[0]
            #self.imgURL = prof.image.url
            self.imgURL = 'images/boruto.jpg'

        return render(request, self.template_name, {'form': form, 'imgURL': self.imgURL})

    def post(self, request):
        form = self.form_class(request.POST)

        if request.user.is_authenticated:
            usr = User.objects.filter(username=request.user.username)[0]
            prof = Profile.objects.filter(username=request.user.username)[0]
            #self.imgURL = prof.image.url
            self.imgURL = 'images/boruto.jpg'

        if form.is_valid():
            rec_username = form.cleaned_data['username']
            rec_password = form.cleaned_data['password']

            user = authenticate(username=rec_username, passwrod=rec_password)
            print(user)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('movie:rated')

        return render(request, self.template_name, {'form': form, 'imgURL': self.imgURL})


def movie_page(request, movie_id):
    imgurl = ''
    rate = request.GET['rate']
    crude = request.GET['crude']
    if request.user.is_authenticated:
        usr = User.objects.filter(username=request.user.username)[0]
        prof = Profile.objects.filter(username=usr)[0]
        #imgurl = prof.image.url
        imgurl = ''

    context = {
        'movie_id': movie_id,
        'imgURL': imgurl,
        'rate': rate,
        'crude': crude
    }
    return render(request, 'movie/movie_page.html', context)


def rated(request):
    global idList, rateList
    idList = []
    rateList = []
    imgurl = ''
    loaded = False
    if request.user.is_authenticated:
        usr = User.objects.filter(username=request.user.username)[0]
        prof = Profile.objects.filter(username=usr)[0]
        imgurl = ''

        if prof.trained:
            print('using trained algorithm')
            u_id = prof.id - 1

            p_rates = PredictionModel.objects.filter(userId=u_id).order_by('-rating')
            rated = UMMat.objects.filter(userId=u_id).exclude(rating=0)

            ratedIds = []
            for i in rated:
                ratedIds.append(i.movieId)
            ratedIds = sorted(ratedIds)
            p_rates = p_rates.exclude(movieId__in=ratedIds)

            for i in p_rates:
                #print(i.movieId, i.rating)
                idList.append(i.movieId)
                rateList.append(i.rating)

            maxR = max(rateList)
            for i in range(len(rateList)):
                rateList[i] /= maxR
                rateList[i] *= 5

        else:
            print('using new user algorithm')
            gender1 = prof.gender
            # print(gender1)
            gender = getGenderChar(gender1)
            # print(gender)
            genderList = list(GenderAvg.objects.filter(gender=gender))

            age1 = prof.age_group
            ageList = list(AgeAvg.objects.filter(ageRange=age1))

            job1 = prof.profession
            job2 = getJobId(job1)
            jobList = list(JobAvg.objects.filter(jobId=job2))

            avgRates = {}
            for i in range(len(genderList)):
                avgRates[i] = (ageList[i].avgRating + genderList[i].avgRating + jobList[i].avgRating) / 3.0

            avgRates = sorted(avgRates.items(), key=op.itemgetter(1), reverse=True)
            idList = [avgRates[i][0] for i in range(len(avgRates))]
            rateList = [avgRates[i][1] for i in range(len(avgRates))]

    return render(request, 'movie/rated.html', {'imgURL': imgurl})


def searchres(request):
    stri = request.GET['key']
    divset = []
    try:
        if stri != "":
            mov = MovieInfo.objects.filter(name__contains=stri)[0:5]

            for indx in mov:
                div = "<div class=\'sres\' onclick=\'imdb_retrieve(this)\' imdb=\'3315342\'><img src=\'" + static(
                    "movie/images/" + indx.poster) + "\' class=\'search_poster\'/><div class=\'sres_des\'>" + str(
                    indx.name) + "<br><span class=\'sres_year\'>" + str(indx.year) + "</span></div></div>"
                divset.append(div)

    except(KeyError, Movies.DoesNotExist):
        return JsonResponse({"divset": [""]})
    else:
        return JsonResponse({"divset": divset})


def getGenderChar(g):
    if g == '1':
        return "M"
    if g == '2':
        return "F"


def requestMovies(request):
    quota = int(request.GET['quota'])
    # gens = request.GET['gens']
    # print(gens)
    divset = []
    if request.user.is_authenticated:
        usr = User.objects.filter(username=request.user.username)[0]
        prof = Profile.objects.filter(username=usr)[0]

        try:
            # mov = MovieInfo.objects.all()[0:15]
            # mov = None
            # print(idList)
            mov = MovieInfo.objects.filter(m_id__in=idList[(15 * (quota - 1)):(15 * quota)])
            num = (quota - 1) * 15
            for indx in mov:
                div = "<div class='poster' onclick='imdb_retrieve(this)' crude='"+ indx.imdb +"' imdb='" + indx.imdb.zfill(7) + "' rate='" + str(int(rateList[num]*20)) + "'><img class='poster_img' src=" + indx.poster + "/><div class=\'shade fades\'></div><div class=\'upper_triangle fades\'></div><span class=\'triangle_rating\'>" + str(int(rateList[num]*20)) + "</span><div class=\'poster_des_container fades\'><div class=\'poster_rating_cover\'><div class=\'poster_rating\'></div></div><span class=\'poster_title\'>" + indx.name + "</span><span class=\'poster_genre\'><br>Drama, Mystery</span></div></div>"
                divset.append(div)
                num += 1

        except(KeyError, Movies.DoesNotExist):
            return JsonResponse({"divset": [""]})
        else:
            return JsonResponse({"divset": divset})
    else:
        try:
            mov = list(MovieInfo.objects.all())

            shuffle(mov)
            # print('else')
            for indx in mov[(15 * (quota - 1)):(15 * quota)]:
                div = "<div class='poster' imdb='0" + indx.imdb + "'><img class='poster_img' src=" + indx.poster + "/><div class=\'shade fades\'></div><div class=\'upper_triangle fades\'></div><span class=\'triangle_rating\'>95</span><div class=\'poster_des_container fades\'><div class=\'poster_rating_cover\'><div class=\'poster_rating\'></div></div><span class=\'poster_title\'>" + indx.name + "</span><span class=\'poster_genre\'><br>Drama, Mystery</span></div></div>"
                divset.append(div)

        except(KeyError, Movies.DoesNotExist):
            return JsonResponse({"divset": [""]})
        else:
            return JsonResponse({"divset": divset})


class userFormView(View):
    form_class = signupForm
    template_name = 'movie/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            rec_username = form.cleaned_data['username']
            rec_password1 = form.cleaned_data['password1']
            rec_firstName = form.cleaned_data['firstName']
            rec_lastName = form.cleaned_data['lastName']
            rec_email = form.cleaned_data['email']
            rec_age = form.cleaned_data['age']
            rec_gender = form.cleaned_data['gender']
            rec_profession = form.cleaned_data['profession']
            rec_country = form.cleaned_data['country']
            rec_image = form.cleaned_data['image']

            user = User.objects.create(username=rec_username)
            user.first_name = rec_firstName
            user.last_name = rec_lastName
            user.email = rec_email
            user.set_password(rec_password1)
            user.save()

            user = authenticate(username=rec_username, password=rec_password1)

            rec_age_group = getGenderGroup(rec_age)

            if user is not None:
                prof = Profile(username=user, age=rec_age, gender=rec_gender,
                               profession=rec_profession, country=rec_country,
                               image=rec_image, age_group=rec_age_group)
                prof.save()

                if user.is_active:
                    login(request, user)
                    return redirect('movie:index')

        return render(request, self.template_name, {'form': form})


class loginPage(View):
    form_class = signinForm
    template_name = 'movie/login.html'
    imgURL = ''

    def get(self, request):
        form = self.form_class(None)

        if request.user.is_authenticated:
            usr = User.objects.filter(username=request.user.username)[0]
            prof = Profile.objects.filter(username=usr)[0]
            self.imgURL = 'images/boruto.jpg'

        return render(request, self.template_name, {'form': form, 'imgURL': self.imgURL})

    def post(self, request):
        form = self.form_class(request.POST)

        if request.user.is_authenticated:
            usr = User.objects.filter(username=request.user.username)[0]
            prof = Profile.objects.filter(username=usr)[0]
            # if len(prof.img.url) > 30:
            self.imgURL = 'images/boruto.jpg'
            # else:
            #    self.imgURL = prof.image.url

        if form.is_valid():
            rec_username = form.cleaned_data['username']
            rec_password = form.cleaned_data['password']

            user = authenticate(username=rec_username, password=rec_password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('movie:rated')

        return render(request, self.template_name, {'form': form, 'imgURL': self.imgURL})


def logoutRequest(request):
    logout(request)
    return JsonResponse({'logged_out': True})


def addRatings(request):
    # file = pd.read_csv('../../res/small/ratings.csv')
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
    context = {}
    p_rates = PredictionModel.objects.filter(userId=u_id).order_by('-rating')
    # for i in p_rates[:10]:
    #    print(i.userId, i.movieId, i.rating)
    # print(len(p_rates))
    rated = UMMat.objects.filter(userId=u_id).exclude(rating=0)
    ratedIds = []
    for i in rated:
        ratedIds.append(i.movieId)
    ratedIds = sorted(ratedIds)
    # print(ratedIds)
    p_rates = p_rates.exclude(movieId__in=ratedIds)
    # print(len(p_rates))
    # for i in p_rates[:10]:
    #    print(i.userId, i.movieId, i.rating)

    mset = []
    rset = []
    for i in p_rates[:10]:
        mov = MovieInfo.objects.get(m_id=i.movieId)
        rr = i.rating
        rr *= 18
        rr = int(rr)
        if rr > 100:
            rr = 100
        mset.append([mov, rr])
    context['movieList'] = mset
    return render(request, 'movie/rated.html', context)


def makeUnrated(request):
    file = pd.read_csv("C:/Users/shp/Desktop/Movie Recommendation system/res/small/userMovieMat.csv")
    arr = file.as_matrix()
    pri = 1
    for i in range(5):  # 501
        userUnrated = np.nonzero(arr[i] == 0)
        print(userUnrated[0])
        for j in userUnrated[0]:
            u = Unrated(user_id=i, movie_id=j)
            print(u, i, j)
            # u.save()
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
        linked[int(mIds[i])] = 'tt' + str(imdbL[i])

    for i in range(len(mIds)):
        try:
            mov = MovieInfo.objects.get(pk=i)
            print(mov.m_id)
            idd = mov.m_id
            print(idd)
            ss = linked[idd]
            print(ss)
            mov.imdb = ss
            # mov.save()
        except:
            print('noooooo')
    return HttpResponse('wooo')


def movieData(request):
    yearList = request.GET['years']
    genreList = request.GET['genres']

    '''years
        2017 : 2017+
        2014 : 2014-16
        2012 : 2012-14
        2007 : 2007-12
        2000 : 2000-07
        1900 : 1900-1999
    '''
    '''genres
        Action
        Adventure
        Animation
        Children's
        Comedy
        Crime
        Documentary
        Drama
        Fantasy
        Film-Noir
        Horror
        Musical
        Mystery
        Romance
        Sci-Fi
        Thriller
        War
        Western
    '''

    allMovies = MovieInfo.objects.all()

    return JsonResponse({'msg': 'not done yet...'})


def movieView(request, m_id):
    try:
        movie = MovieInfo.objects.get(pk=m_id)
        context = {
            'movie': movie
        }
        return render(request, 'movie/movie_page.html', context)
    except:
        return Http404("Movie Not Found!")


def ratedView(request):
    return HttpResponse('rated')


def signUpView(request):
    return render(request, 'movie/signup.html', {})


def userView(request):
    return render(request, 'movie/user.html', {})


def catView(request):
    return render(request, 'movie/category.html', {})


def getGenderGroup(age):
    if age < 18:
        return "Unser 18"
    elif age < 25:
        return "18-24"
    elif age < 35:
        return "25-34"
    elif age < 45:
        return "35-44"
    elif age < 50:
        return "45-49"
    elif age < 56:
        return "50-55"
    else:
        return "56+"


def getJobId(job):
    if type(job) == int:
        return job
    else:
        if job == 'other':
            return 0
        elif job == 'academic/educator':
            return 1
        elif job == 'artist':
            return 2
        elif job == 'clerical/admin':
            return 3
        elif job == 'college/grad student':
            return 4
        elif job == 'customer service':
            return 5
        elif job == 'doctor/health care':
            return 6
        elif job == 'executive/managerial':
            return 7
        elif job == 'farmer':
            return 8
        elif job == 'homemaker':
            return 9
        elif job == 'K-12 student':
            return 10
        elif job == 'lawyer':
            return 11
        elif job == 'programmer':
            return 12
        elif job == 'retired':
            return 13
        elif job == 'sales/marketing':
            return 14
        elif job == 'scientist':
            return 15
        elif job == 'self-employed':
            return 16
        elif job == 'technician/engineer':
            return 17
        elif job == 'tradesman/craftsman':
            return 18
        elif job == 'unemployed':
            return 19
        else:
            return 20


def transferOldUsers(request):
    userList = list(Users.objects.all())

    for i in range(1, len(userList)):
        rec_username = "johnDoe" + str(i)
        rec_password1 = "qwerty123"
        rec_firstName = userList[i].first_name
        rec_lastName = userList[i].last_name
        rec_email = 'email@email.com'
        rec_age = userList[i].age
        if userList[i].gender == 'M':
            rec_gender = 1
        else:
            rec_gender = 2
        rec_profession = userList[i].occupation
        rec_country = userList[i].country
        rec_image = 'images\\boruto.jpg'

        user = User.objects.create(username=rec_username)
        user.first_name = rec_firstName
        user.last_name = rec_lastName
        user.email = rec_email
        user.set_password(rec_password1)
        user.save()
        # print('saved user')

        user = authenticate(username=rec_username, password=rec_password1)

        rec_age_group = getGenderGroup(rec_age)

        if user is not None:
            prof = Profile(username=user, age=rec_age, gender=rec_gender,
                           profession=rec_profession, country=rec_country,
                           image=rec_image, age_group=rec_age_group)
            prof.save()
            # print('saved')

    return Http404()


def setLiking(request):
    crude = request.GET['crude']
    rate = request.GET['rate']
    print(crude, rate)

    if request.user.is_authenticated:
        usr = User.objects.filter(username=request.user.username)[0]
        #prof = Profile.objects.filter(username=usr)[0]
        id = usr.id
        u_id = id - 1
        usr2 = Users.objects.get(pk=u_id)
        mov = MovieInfo.objects.get(imdb=crude)

        r = Ratings(
            user=usr2,
            movie=mov,
            rating=int(rate)
        )

        r.save()

    return JsonResponse({'output': True})
