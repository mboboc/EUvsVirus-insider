from app import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.SignupView.as_view(), name='signup'),
]