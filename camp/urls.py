from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('employment', views.employment, name='employment'),
    path('loginhome', views.login_home, name='loginhome'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contactus, name='contact'),
    path('feedback', views.feedback, name='feedback'),
    path('details', views.details, name='details'),
    path('add_details', views.add_details, name='add_details'),
    path('add_event', views.add_event, name='add_event'),
    path('add_employment', views.add_employment, name='add_employment'),
    path('eventlist', views.events, name='eventlist'),
    path('feedbacktable', views.feedbacks, name='feedbacktable'),
    path('viewpro', views.viewpro, name='viewpro'),
    path('editpro', views.editpro, name='editpro')
]
