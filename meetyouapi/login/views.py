from django.shortcuts import render

# Create your views here.

def login(request):
    if request.method == "POST"
    user_code = request.POST.code
    print(user_code)
