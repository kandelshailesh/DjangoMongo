# from django.contrib.auth.views import logout
from django.urls import path
from . import views


urlpatterns = [
    # path('',views.final,name='final'),
    path('', views.index, name='index'),
    
    # path('delete',views.deletemessage,name='deletemessage'),
]
