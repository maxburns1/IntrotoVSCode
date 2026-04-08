from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # Explicitly define logout before the include to override any defaults
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Registration page
    path('register/', views.register, name='register'),
    
    # Include default auth urls (login, etc.)
    path('', include('django.contrib.auth.urls')),
]