from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/show.html')

def showpage(request):
    return render(request, 'main/mainpage.html')
