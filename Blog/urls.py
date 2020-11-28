from django.urls import path
from . import views
from .views import*
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogView.as_view(), name = 'Blog'),
    path('PostListView/', PostListView.as_view(), name = 'PostListView'),
    path('PostListView/<int:pk>/', PostView.as_view(), name = 'Post'),
    path('Register/', views.Register, name = 'Register'),
    path('Login/', auth_views.LoginView.as_view(template_name = 'Login.html'), name = 'Login'),
    path('Logout/', auth_views.LogoutView.as_view(next_page = '/'), name = 'Logout'),
]