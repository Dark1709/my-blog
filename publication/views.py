from django.shortcuts import render

# Create your views here.


def hi_publication(request):
    return render(request, 'publication/publication.html')
