from django.contrib import admin
from django.urls import path,include
from Bihar_trend import views
urlpatterns = [
   
    path("makeKpiTrend/old/",views.old_bih_trend),
    # path("logout/",views.logout, name="logout"),


]