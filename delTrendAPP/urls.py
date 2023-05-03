from django.urls import path
from . import views


urlpatterns = [
   path("makeKpiTrend/old/4G",views.old_del4G_trend),
   path("makeKpiTrend/old/2G",views.old_del2G_trend),




 
]