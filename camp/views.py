from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Organizer,Job_Description,cityevents,ContactUs,Feedback,ProgramDetails
from django.shortcuts import redirect

# Create your views here.
def home(request):   
    eventset=cityevents.objects.all().order_by('-date')[:5]
    context={'dict':eventset}
    feedbackset=Feedback.objects.all().order_by('-Rating')[:3]
    context1={'dict1':feedbackset}
    return render(request,'camp/home.html', {'dict':eventset,'dict1':feedbackset})

####Registration Page#######
def registration(request):
    print(request.POST)
    if request.method=="POST":
        campmail=request.POST["campmail"]
        camppass=request.POST["camppass"]
        campadd=request.POST["campadd"]
        campname=request.POST["campname"]
        campowner=request.POST["campowner"] 
        campphone=request.POST["campphone"] 
        description=request.POST["description"] 
        Organizer_obj=Organizer(SummerCamp_Id=campmail, Password=camppass, CampName=campname, OwnerName=campowner, CampPhone=campphone, CampAddress=campadd, Description=description)
        Organizer_obj.save()
        messages.success(request, "Registration Successful!")
    return render(request,'camp/registration.html')
def contactus(request):
    print("hello")
    print(request.POST)
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["mailid"]
        phone=request.POST["phone"]
        date=request.POST["date"]
        query=request.POST["query"]
        contact_obj=ContactUs(name=name, email=email, phone=phone, query=query, date=date)
        contact_obj.save()
        messages.success(request, "Our Team reach you early!")
        print(name)
    return render(request,'camp/contact.html')

def feedback(request):
    print(request.POST)
    if request.method=="POST":
        name=request.POST["name"]
        campname=request.POST["campname"]
        date=request.POST["date"]
        email=request.POST["mail"]
        feedback=request.POST["feedback"]
        rating=request.POST["rating"]
        feed_obj=Feedback(Name=name,Email=email,CampName=campname,Date=date,FeedbackText=feedback,Rating=rating)
        feed_obj.save()
        messages.success(request, "THANK YOU!")
    return render(request,'camp/feedback.html')

def login(request):
    if request.method=="GET":
        return render(request,'camp/login.html')
    if request.method=="POST":
        s_id=request.POST["mailid"]
        print(s_id)
        password=request.POST["usrpass"]
        Organizer_obj=Organizer.objects.filter(SummerCamp_Id=s_id,Password=password)
        if len(Organizer_obj)>0:
            request.session["session_id"]=s_id
            context={"organizer_data":Organizer_obj}
            return render(request,'camp/login_home.html',context)
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("login")

def login_home(request):
    s_id=request.session["session_id"]
    organizer_obj=Organizer.objects.filter(SummerCamp_Id=s_id)
    context={"organizer_data":organizer_obj}
    print("loggedin successfully")
    return render(request,'camp/login_home.html',context)

def viewpro(request):
    s_id=request.session["session_id"]
    pd=ProgramDetails.objects.filter(SummerCamp_Id=s_id)
    context={'proinfo':pd}
    return render(request, 'camp/viewprogram.html', context)

def logout(request):
    del request.session["session_id"]
    return render(request, 'camp/login.html')

def employment(request):
    st=Job_Description.objects.all()
    context={"stinfo":st}
    return render(request, 'camp/employment.html',context)

def details(request):
    pd=ProgramDetails.objects.all()
    context={'proinfo':pd}
    return render(request, 'camp/programdetails.html', context)

def add_details(request):
    print(request.POST)
    if request.method=="POST":
        s_id=request.session["session_id"]
        print(s_id)
        org=Organizer(SummerCamp_Id=s_id)      
        ProgramName=request.POST["proname"]
        Duration=request.POST["duration"]
        Fees=request.POST["fee"]
        StartDate=request.POST["start"]
        EndDate=request.POST["end"] 
        AgeGroup=request.POST["age"] 
        description=request.POST["description"] 
        program_obj=ProgramDetails(SummerCamp_Id=org,ProgramName=ProgramName,Duration=Duration,Fees=Fees,StartDate=StartDate,EndDate=EndDate,Description=description,AgeGroup=AgeGroup)
        program_obj.save()
        messages.success(request, "Program Added!")
        context={'dict':org}
    return render(request, 'camp/add_details.html')

def add_event(request):
    print(request.POST)
    if request.method=="POST":
        s_id=request.session["session_id"]
        # Summercampid=request.POST["scampid"]
        EventName=request.POST["evname"]
        Address=request.POST["evadd"]
        City=request.POST["evcity"]
        Date=request.POST["evdate"]
        # EndDate=request.POST["end"] 
        Eventpic=request.POST["evimg"] 
        description=request.POST["evdescription"] 
        event_obj=cityevents(event_name=EventName,date=Date,city=City,address=Address,description=description,event_pic=Eventpic)
        event_obj.save()
        messages.success(request, "Event Added!")
    return render(request, 'camp/add_event.html')
    
def add_employment(request):
    if request.method=="POST":
        print('hello')
        summercapid=request.session["session_id"]
        print(summercapid)
        org=Organizer(SummerCamp_Id=summercapid)      
        jobid=request.POST["jobid"]
        postname=request.POST["postname"]
        noofseats=request.POST["seats"]
        applydate=request.POST["apply"]
        postdate=request.POST["post"]
        description=request.POST["jobdescription"]
        job_obj=Job_Description(SummerCamp_Id=org,job_id=jobid,postname=postname,NoOfSeats=noofseats,LastDateToApply=applydate,PostDate=postdate,JobDescription=description)
        job_obj.save()
        messages.success(request, "Added Successfully!")
    return render(request, 'camp/add_employment.html')

def events(request):
    ev=cityevents.objects.all()
    context={'events':ev}
    return render(request,'camp/more_events.html',context)

def feedbacks(request):
    feedbackset=Feedback.objects.all()[:3]
    context={'dict1':feedbackset}
    return render(request, 'camp/feedbacktable.html',context)

def editpro(request):
    if request.method=='GET':
        s_id=request.session["session_id"]
        orga=Organizer.objects.get(SummerCamp_Id=s_id)
        context={'info':orga}
        return render(request, 'camp/editpro.html',context)
    print(request.POST)
    if request.method=="POST":
        s_id=request.session["session_id"]
        organizer_obj=Organizer.objects.filter(SummerCamp_Id=s_id)
        org=Organizer(SummerCamp_Id=s_id)
        context={"organizer_data":organizer_obj}
        camppass=request.POST["newpass"]
        campadd=request.POST["newadd"]
        CampName=request.POST["newcamp"]
        campowner=request.POST["newowner"] 
        campphone=request.POST["newphone"] 
        description=request.POST["description"] 
        Organizer_obj=Organizer(SummerCamp_Id=org,Password=camppass, CampName=CampName, OwnerName=campowner, CampPhone=campphone, CampAddress=campadd, Description=description)
        Organizer_obj.save()
        messages.success(request, "Update Successful!")
        return render(request, 'camp/login_home.html',context)