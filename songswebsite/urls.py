# from django.contrib import admin
# from django.urls import path
# from lyrics import views

 
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('songs/', views.song_list, name='song_list'),
#     path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path
from lyrics import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('songs/', views.song_list, name='song_list'),
    path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
    path('admin/', admin.site.urls),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
