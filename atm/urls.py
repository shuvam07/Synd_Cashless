from django.conf.urls import  url

from . import views

app_name = 'atm'

urlpatterns = (
    url(r'home/$', views.home,name='home'),
    url(r'cardless/$', views.cardless,name='cardless'),
    url(r'verifyOTP/$', views.verifyOTP,name='verifyOTP'),
    url(r'card/$', views.card,name='card'),
    url(r'view_screen/$',views.view_screen,name='view_screen'),
    url(r'checkValidAndOTP/$',views.checkValidAndOTP,name='checkValidAndOTP'),
)