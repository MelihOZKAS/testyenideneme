from django.shortcuts import render,HttpResponse,get_object_or_404,reverse

from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import re
from django.views import View
from .models import *
import json
from django.db import IntegrityError
from django.http import JsonResponse

def home3(request):
    user_agent = request.META.get('HTTP_USER_AGENT').lower()

    if 'amphtml' in user_agent or 'mobile' in user_agent or 'safari' in user_agent in user_agent:
        # Mobil cihaz ise AMP sayfasına yönlendir
        return render(request, 'amp/blog.amp.html')
    else:
        # Masaüstü cihaz ise normal sayfaya yönlendir
        return HttpResponse(f'Sitemiz Şu an Yapımda')





def home(request):
    user_agent = request.META['HTTP_USER_AGENT']

    # Mobil cihazları tanımlayan bir regex deseni
    mobile_regex = r".*(iphone|mobile|androidtouch)"

    # Kullanıcı ajanını kontrol edin
    if re.match(mobile_regex, user_agent, re.I):
        return render(request, 'amp/blog.amp.html')
    else:
        return HttpResponse(f'Sitemiz Şu an Yapımda')



class StoryPreviewView(View):
    def get(self, request, *args, **kwargs):
        story = Kontrol.objects.get(slug=kwargs['slug'])

        # Veritabanından bilgileri çek
        title = story.title
        h1 = story.h1
        keywords = story.keywords
        description = story.meta_description

        # İçeriği oluştur
        content = f"Title: {title}\n\n <br> H1: {h1}\n\n <br> Keywords: {keywords}\n\n <br> Description: {description}\n\n <br> {story.icerik} \n\n  "

        return HttpResponse(content)


def Enderun(request, post_slug):
    user_agent = request.META.get('HTTP_USER_AGENT').lower()
    PostEndrun = get_object_or_404(Kontrol, slug=post_slug)

    title = PostEndrun.title
    H1 = PostEndrun.h1
    description = PostEndrun.meta_description
    keywords = PostEndrun.keywords

    context = {
        'title': title,
        'H1': H1,
        'description': description,
        'keywords': keywords,
        'PostEndrun': PostEndrun,
    }

    if 'amphtml' in user_agent or 'mobile' in user_agent or 'safari' in user_agent in user_agent:
        # Mobil cihaz ise AMP sayfasına yönlendir
        return render(request, 'amp/blog.amp.html', context)
    else:
        # Masaüstü cihaz ise normal sayfaya yönlendir
        return HttpResponse(f'Sitemiz Şu an Yapımda')


def EnderunNew(request, post_slug):
    user_agent = request.META.get('HTTP_USER_AGENT').lower()
    PostEndrun = get_object_or_404(Kontrol, slug=post_slug)

    title = PostEndrun.title
    H1 = PostEndrun.h1
    description = PostEndrun.meta_description
    keywords = PostEndrun.keywords

    context = {
        'title': title,
        'H1': H1,
        'description': description,
        'keywords': keywords,
        'PostEndrun': PostEndrun,


    }

    if 'amphtml' in user_agent or 'mobile' in user_agent or 'safari' in user_agent in user_agent:
        # Mobil cihaz ise AMP sayfasına yönlendir
        return render(request, 'amp/new-enderun.amp.html', context)
    else:
        # Masaüstü cihaz ise normal sayfaya yönlendir
        return HttpResponse(f'Sitemiz Şu an Yapımda')


@csrf_exempt
def mahsulyakala(request):
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            for item in data:
                Main_Link = item.get('Main_Link')
                Post_Link = item.get('Post_Link')
                try:
                    mahsulkayit = Mahsul(Tarla_Link=Main_Link, Mahsul_Link=Post_Link, Akibeti='Beklemede')
                    mahsulkayit.save()
                except IntegrityError:
                    continue  # Bu satırı ekledim.
            return JsonResponse({"message": "Başarılı"})
        else:
            return JsonResponse({"error": "Geçersiz Content-Type başlığı"}, status=400)
    else:
        return JsonResponse({"method": request.method, "headers": dict(request.headers)})

@csrf_exempt
def mahsullistesicek(request):
    if request.method == 'POST':
        tarla_link = request.POST.get('Tarla_Link')
        mahsul_list = Mahsul.objects.filter(Tarla_Link=tarla_link).order_by('-olusturma_tarihi')[:150]
        mahsul_links = "|".join([mahsul.Mahsul_Link for mahsul in mahsul_list])
        return HttpResponse(mahsul_links)
    else:
        return HttpResponse("Geçersiz istek", status=400)