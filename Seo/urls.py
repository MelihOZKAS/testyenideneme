from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("mahsul-yakala/", views.mahsulyakala),
    path("mahsul-listesi-cek/", views.mahsullistesicek),
    path('story-preview/<slug:slug>/', views.StoryPreviewView.as_view(), name='story_preview'),
    path('<str:post_slug>/', views.Enderun, name='post-getir'),#Blog Git
    path('new/<str:post_slug>/', views.EnderunNew, name='post-getir-new'),#Blog Git

   ]

