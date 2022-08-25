from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('albums/<int:pk>', views.album_detail, name='album_detail'),
    path('albums/new/', views.create_album, name='create_album'),
    path('albums/<int:pk>/edit/', views.album_edit, name='album_edit'),
]