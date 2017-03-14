from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Movies
from django.contrib.staticfiles.templatetags.staticfiles import static

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