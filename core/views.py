from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
    return render(request, 'layout/index.html')

def register_view(request):
    return render(request, 'layout/register.html')

def donor_view(request):
    return render(request, 'layout/donor_list.html')