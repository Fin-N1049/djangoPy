from django.shortcuts import render

def create(request):
    return render(request, 'create.html')

def list(request):
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
    return render(request, 'list.html')
    
def edit(request):
    return render(request, 'edit.html')