from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("mahsul-yakala/", views.mahsulyakala),
    path("mahsul-listesi-cek/", views.mahsullistesicek),
    path("add-post/", views.post_add),
    path("mahsul-cek/", views.mahsulcek),
    path("ai-cek/", views.ai_cek),
    path("ai-makale-cek/", views.ai_makale_cek),
    path("ai-cek-alt/", views.ai_cek_Alt_Baslik_Cek),
    path("ai-add/", views.ai_add),
    path("ai-alt-add/", views.ai_alt_baslik_add),
    path('story-preview/<slug:slug>/', views.StoryPreviewView.as_view(), name='story_preview'),
    path('<str:post_slug>/', views.Enderun, name='post-getir'),#Blog Git
    path('new/<str:post_slug>/', views.EnderunNew, name='post-getir-new'),#Blog Git

   ]

