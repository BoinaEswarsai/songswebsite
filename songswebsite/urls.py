from django.contrib import admin
from django.urls import path
from lyrics import views

 
urlpatterns = [
    path('', views.home, name='home'),
    path('songs/', views.song_list, name='song_list'),
    path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
    path('admin/', admin.site.urls),
]
