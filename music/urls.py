from django.urls import path
from . import views

urlpatterns = [
	#/music/
    path('', views.index, name ='index'),
    #/721/
    path('<int:album_id>/', views.details, name="details"),
]

