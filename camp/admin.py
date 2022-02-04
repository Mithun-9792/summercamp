from django.contrib import admin
from.models import  cityevents,Organizer,ContactUs,Job_Description,ProgramDetails,Feedback

#Register your models here.
admin.site.register(cityevents)
admin.site.register(Organizer)
admin.site.register(ContactUs)
admin.site.register(Job_Description)
admin.site.register(ProgramDetails)
admin.site.register(Feedback)

