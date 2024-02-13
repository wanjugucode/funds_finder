from django.db import models

# Create your models here.
class Scholarships(models.Model):
    name= models.CharField(max_length=255,blank=True, null=True)
    description= models.TextField(blank=True, null=True)
    eligibility_criteria= models.TextField(blank=True, null=True)
    scholarship_type= models.CharField(max_length=50, choices=[('merit', 'Merit-Based'), ('need', 'Need-Based')],blank=True, null=True)
    status= models.CharField(max_length=50, choices=[('open', 'Open'), ('closed', 'Closed'), ('ongoing', 'Ongoing')],blank=True, null=True)
    application_deadline = models.DateTimeField(blank=True, null=True)
    Contact_email=models.EmailField(blank=True, null=True)
    id= models.IntegerField(primary_key=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)


class ScholarshipApplication(models.Model):
    user= models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='scholarships',null=True)
    essay= models.TextField(null=True)
    created_at= models.DateTimeField(auto_now_add=True,null=True)
    is_approved= models.BooleanField(default=False,null=True)  # New field for approval status
    id= models.IntegerField(primary_key=True,null=False)
    scholarship= models.ForeignKey(Scholarships, on_delete=models.CASCADE, related_name='applications',null=True )
    approved_scholarship=models.ForeignKey('scholarships.ApprovedScholarship', on_delete=models.CASCADE, related_name='applyscholarship',null=True)


    
class ApprovedScholarship(models.Model):
    original_application = models.OneToOneField(ScholarshipApplication, on_delete=models.CASCADE, related_name='approved_application',null=False)
    approval_date = models.DateTimeField(auto_now_add=True,null=True
    )

    def __str__(self):
        return f"Approved Application for {self.original_application.name}"


class Bookmark(models.Model):
    user = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='bookmarks')
    scholarship = models.ForeignKey(Scholarships, on_delete=models.CASCADE, related_name='bookmarks', null=True)