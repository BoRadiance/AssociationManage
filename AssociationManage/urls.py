"""AssociationManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from AssMan.views import showarticle,adminarticle,admindepart,adminpeople
from AssMan.views import addarticle,adddepart,addpeople
from AssMan.views import articledetail,editarticle,delarticle
from AssMan.views import deldepart,editdepart
from AssMan.views import delpeople,editpeople

urlpatterns = [
    path('',showarticle),
    path('adminarticle',adminarticle),
    path('admindepart',admindepart),
    path('adminpeople',adminpeople),
    path('addarticle',addarticle),
    path('adddepart', adddepart),
    path('addpeople', addpeople),
    path('articledetail/<int:pid>',articledetail),
    path('delarticle/<int:pid>',delarticle),
    path('editarticle/<int:pid>',editarticle),


    path('deldepart/<int:pid>',deldepart),
    path('editdepart/<int:pid>',editdepart),



    path('delpeople/<int:pid>',delpeople),
    path('editpeople/<int:pid>',editpeople),


]
