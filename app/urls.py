from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register/',views.register,name="register"),
    path('home/',views.userhome,name='home'),
    path('profile/',views.profile,name="profile"),
    path('history/',views.history,name="history"),
    path('logout/',views.logout,name='logout')

]
