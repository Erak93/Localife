from django.shortcuts import render

# Create your views here.



def post_app(request):
    return render(request,'post_app/post_app.html')