from django.urls import path
from . import views


urlpatterns = [
   path("makeKpiTrend/old/",views.old_del_trend),
   # path("makeKpiTrend/old/2G",views.old_del2G_trend),




 
]