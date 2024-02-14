# profiles/views.py
from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserProfileForm
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def add_profile(request):
    # Check if the user already has a profile
    if UserProfile.objects.filter(user=request.user).exists():
        return redirect('viewprofile')  # Redirect to the viewprofile page or another appropriate location
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('viewprofile')  # Redirect to the viewprofile page or another appropriate location
        else:
            print(form.errors)
    else:
        form = UserProfileForm()
    return render(request, "add_profile.html", {"form": form})

@login_required
def edit_profile(request, id):
    profile = UserProfile.objects.get(id=id)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            if form.is_valid():
                form.save()    
                return redirect('viewprofile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {"form": form})

@login_required
def delete_profile(request, id):
    profile = get_object_or_404(UserProfile, id=id)
    # Check if the user trying to delete the profile is the owner
    if request.user != profile.user:
        return redirect('error_page')  # Redirect to an error page or another appropriate location
    if request.method == 'POST':
        profile.delete()
        return redirect('home')  # Redirect to the home page or another appropriate location
    return render(request, 'delete_profile.html', {'profile': profile})

@login_required
def dashboard(request):
    return render(request,"dashboard.html")

@login_required
def view_profile(request):
    profile=UserProfile.objects.all()
    return render(request,"view_profile.html",{ "profile":profile})
