from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register/',views.register,name="register"),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name="profile"),
    path('history/',views.history,name="history"),
    path('logout/',views.logout,name='logout'),
    path('users/',views.users,name='users'),
    path('prime/',views.prime,name='prime'),
    path('staff/',views.staff,name='staff'),
    path('addstaff/',views.addstaff,name='addstaff'),
    path('adduser/',views.adduser,name='adduser'),
    path('edituser/<int:id>/',views.edituser,name='edituser'),
    path('addprimuser/<int:id>/',views.addprimeuser,name='addprimeuser'),
    path('editprimeuser/<int:id>/',views.editprimeuser,name='editprimeuser'),
    path('delete/<int:id>/<str:value>/',views.delete,name='delete')

]
