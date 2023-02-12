from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.db.models import Q

from .models import MAIN_LINKS, TOP_BAR_LINKS, Electronicparts, Storage, Categories
# Create your views here.



top_bar_quick_links ={}


for main_link in MAIN_LINKS.objects.all():
    top_bar_quick_links[main_link.main_name] = []
    for top_bar_link in TOP_BAR_LINKS.objects.filter(main=main_link):
        top_bar_quick_links[main_link.main_name].append(top_bar_link.top_bar_name)


electronicParts = Electronicparts.objects.all()

content = [electronicParts, top_bar_quick_links, Storage.objects.all(), Categories.objects.all()]

class IndexView(generic.ListView):

    template_name = './mainpage/index.html'
    context_object_name = 'content'

    def get_queryset(self):
        return content

class SearchResultsView(generic.ListView):
    model = Electronicparts
    template_name = './mainpage/search.html'
    context_object_name = 'content'
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Electronicparts.objects.filter(
            Q(part__icontains=query) | Q(category__name__icontains=query) | Q(room_num__room__icontains=query) | Q(room_num__shortname__icontains=query) | Q(room_num__longname__icontains=query) | Q(room_num__responsible_person__icontains=query) | Q(room_num__title_en__icontains=query) | Q(room_num__title_de__icontains=query)
        )
        content[0] = object_list
        return content 