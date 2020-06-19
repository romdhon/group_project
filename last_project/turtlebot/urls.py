from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeTemplateView.as_view(), name='home'),
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogout, name="logout"),
    path('getting_start/', views.getting_start, name="get_start"),
]