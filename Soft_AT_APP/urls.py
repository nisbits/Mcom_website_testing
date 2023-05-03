from django.urls import path
from Soft_AT_APP.views import *

urlpatterns = [
    path('upload/',SoftAt_Report_Upload),
    path('view/',SoftAt_Circlewise_Dashboard),
    
]