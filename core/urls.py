from operator import index
from django.urls import path
from core.views import SignUpView, ProfileView, Index
from core.views import sendanemail
from .import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('send/', sendanemail, name="email"),
    path('Index/', views.Index , name="Index"),
]