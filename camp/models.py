from django.db import models
from django.utils import timezone

# Create your models here.   
class cityevents(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=50)
    date=models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    address=models.TextField(max_length=50, default="lucknow")
    description=models.TextField(null=True)
    event_pic=models.ImageField(upload_to="camp/eventimg", max_length=1000, null=True)
    def __str__(self):
        return self.event_name

class Organizer(models.Model):
    SummerCamp_Id=models.CharField(primary_key=True, max_length=50)
    Password=models.CharField(null=False, max_length=45)
    CampName=models.CharField(null=False, max_length=50)
    OwnerName=models.CharField(null=False, max_length=40)
    # CampMailId=models.CharField(null=False, max_length=50)
    CampPhone=models.CharField(null=False, max_length=10)
    CampAddress=models.CharField(null=False, max_length=100)
    Description=models.TextField(null=False)
    def __str__(self): 
        return self.SummerCamp_Id
    
class ContactUs(models.Model):
    name=models.CharField(null=False, max_length=50)
    email=models.EmailField(null=True, max_length=30)
    phone=models.CharField(null=False, max_length=10)
    query=models.TextField(null=False)
    date=models.DateField(null=False)
    def __str__(self):
        return self.name

class Job_Description(models.Model):
    SummerCamp_Id=models.ForeignKey(Organizer, on_delete=models.CASCADE)
    job_id=models.CharField(primary_key=True, max_length=50)
    postname=models.CharField(null=False, max_length=50)
    NoOfSeats=models.IntegerField(null=False)
    LastDateToApply=models.DateField(null=False)
    PostDate=models.DateField(null=False)
    JobDescription=models.TextField(null=False)
    def __str__(self):
        return self.postname
    

class ProgramDetails(models.Model):
    SummerCamp_Id=models.ForeignKey(Organizer, on_delete=models.CASCADE)
    ProgramId=models.AutoField(primary_key=True)
    ProgramName=models.CharField(null=False, max_length=30)
    Duration=models.CharField(null=False, max_length=20)
    Fees=models.CharField(null=False, max_length=30)
    StartDate=models.DateField(null=False)
    EndDate=models.DateField(null=False)
    Description=models.TextField(null=False)
    AgeGroup=models.CharField(null=False, max_length=20)
    def __str__(self):
        return self.ProgramName

class Feedback(models.Model):
    FeedbackId=models.AutoField(primary_key=True)
    Name=models.CharField(null=False, max_length=50)
    Email=models.EmailField(null=False, max_length=45)
    CampName=models.CharField(null=False, max_length=50)
    Date=models.DateField(null=False)
    FeedbackText=models.TextField(null=False)
    Rating=models.IntegerField(null=False)
    def __str__(self):
        return self.Name








