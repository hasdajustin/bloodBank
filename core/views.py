from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Donor

# Create your views here.
def home_view(request):
    return render(request, 'layout/index.html')

def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        blood_group = request.POST.get("blood_group")

        # Save at database
        donor = Donor(
            full_name=full_name,
            age=age,
            gender=gender,
            address=address,
            phone=phone,
            email=email,
            blood_group=blood_group,
        )
        donor.save()

        messages.success(request, "Donor registered successfully!")
        return redirect("donor")
    return render(request, 'layout/register.html')

def donor_view(request):
    return render(request, 'layout/donor_list.html')