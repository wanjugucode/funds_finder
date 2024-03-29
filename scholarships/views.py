import os
from django.shortcuts import get_object_or_404, render,redirect
from .forms import *
from .models import Scholarships

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")
def dashboard(request):
    return render(request,"dashboard.html")
def navbar(request):
    return render(request,"navbar.html")

def add_scholarship(request):
    if request.method == "POST":
        form = ScholashipAdditionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_scholarships_view') 
        else:
            print(form.errors)
    else:
        form = ScholashipAdditionForm()

    return render(request, "add_scholarship.html", {"form": form})

def scholarships_list(request):
    scholarships=Scholarships.objects.all()
    return render(request,"scholarship_list.html",{ "scholarship":scholarships})

def admin_scholarships_view(request):
    scholarships=Scholarships.objects.all()
    return render(request,"admin_scholarships_view.html",{ "scholarship":scholarships})



def edit_scholarship(request, id):  
    scholarship = Scholarships.objects.get(id=id)

    if request.method == "POST":
        form = ScholashipAdditionForm(request.POST, request.FILES, instance=scholarship)
        if form.is_valid():
            form.save()       
    else:
        form = ScholashipAdditionForm(instance=scholarship)

    return render(request, 'edit_scholarship.html', {"form": form})
def remove_scholarship(request, id):
    scholarship = Scholarships.objects.get(id=id)

    if request.method == "POST":
        scholarship.delete()

        return redirect('admin_scholarships_view')  
    else:
        return render(request, 'remove_scholarship.html', {'scholarship': scholarship})
    
def apply_scholarship(request):
    if request.method == 'POST':
        form = ScholarshipApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scholarships')  
    else:
        form = ScholarshipApplicationForm()

    return render(request, 'apply_scholarship.html', {'form': form})

def applicants_list(request):
    scholarship_applications = ScholarshipApplication.objects.all()
    return render(request, 'applicants_list.html', {'scholarship_applications': scholarship_applications})
# views.py
# def applicants_list(request):
#     scholarship_applications = ScholarshipApplication.objects.filter(is_approved=False)
#     return render(request, 'applicants_list.html', {'scholarship_applications': scholarship_applications})
def approve_scholarship(request, id):
    # Get the scholarship application or return a 404 response if not found
    application = get_object_or_404(ScholarshipApplication, id=id)

    # Check if the application is not already approved
    if not application.is_approved:
        # Mark the original application as approved
        application.is_approved = True
        application.save()

        # Create a corresponding entry in the ApprovedScholarship model
        ApprovedScholarship.objects.create(original_application=application)

    # Redirect to the list of applicants after approval
    return redirect('applicants_list')
def approved_list(request):
    approved_applications = ApprovedScholarship.objects.all()
    return render(request, 'approved_list.html', {'approved_applications': approved_applications})