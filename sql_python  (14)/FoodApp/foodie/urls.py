from django.contrib import admin
from django.urls import path, include
from foodie import views
urlpatterns = [
    path("display/" ,views.display_name , name="display"),
    path('newdisplay/',views.home,name="home" ),
    path("yogacalculator/" , views.calorie_Yoga_meter , name="calorie meter")
]
