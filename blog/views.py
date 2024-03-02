from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,template_name= 'blog/index.html')

def  test_fun(request):
    return render(request,template_name= 'blog/index.html')