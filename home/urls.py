from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("science", views.science, name="science"),
    path("maths", views.maths, name="maths"),
    path("gk", views.gk, name="gk"),
    path('signup', views.signup, name="signup"),
    path('result/', views.result, name="result"),
    path('get_result', views.get_result_view, name='get_result'),

]