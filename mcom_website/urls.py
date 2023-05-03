"""mcom_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from trend import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('admin/', admin.site.urls),
    # path('',views.index,name="main"),
    path('trend/', include("trend.urls")),
    path('trend/OriginalTrend/', include("Original_trend.urls")),
    path('accounts/', include("accounts.urls")),
    path('trend/bih/', include("Bihar_trend.urls")),
    path('trend/raj/', include("rajTrendAPP.urls")),
    path('trend/kol/', include("kolTrendAPP.urls")),
    path('vendor_management/', include("vendor_management.urls")),
    path('Soft_At/',include("Soft_AT_APP.urls")),
    path('trend/hr/',include("hrTrendAPP.urls")),
    path('trend/ap/',include("apTrendAPP.urls")),
    path('trend/pb/',include("pbTrendAPP.urls")),
    path('trend/del/',include('delTrendAPP.urls'))
   
    

   


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)