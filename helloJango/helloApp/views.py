from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def printHello(request):
    movie_data={
        'movies' :[
        {
            'title':'The Shawshank Redemption',
            'year':1994,
            'summary':'story of a man'
        },
        {
            'title':'Fight Club',
            'year':1999,
            'summary':'story of fighting'
        },
        {
            'title':'Inception',
            'year':2010,
            'summary':'story of dreams'
        }
        ]
    }
    return render(request,'hello.html',movie_data)
