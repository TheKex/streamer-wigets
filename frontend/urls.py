from django.urls import path, include

from frontend import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('/login/', views.login, name='login'),
    path('/logout/', views.logout, name='logout'),
    path('/register/', views.register, name='create'),
]