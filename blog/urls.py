from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.article_list, name='article_list'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('view/', views.search_view, name='search_view'),
]
