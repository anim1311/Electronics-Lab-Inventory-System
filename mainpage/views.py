from sre_parse import CATEGORIES
from django.views import generic
from django.db.models import Q
from django.shortcuts import render
from django.http import FileResponse, HttpResponse, HttpRequest
import os

from .models import MAIN_LINKS, TOP_BAR_LINKS, Electronicparts, Storage, Categories
# Create your views here.



top_bar_quick_links ={}


def refresh_top_bar_quick_links():
    for main_link in MAIN_LINKS.objects.all():
        top_bar_quick_links[main_link.main_name] = []
        for top_bar_link in TOP_BAR_LINKS.objects.filter(main=main_link):
            top_bar_quick_links[main_link.main_name].append(top_bar_link.top_bar_name)



content = [Electronicparts.objects.all(), top_bar_quick_links, Storage.objects.all(), Categories.objects.all()]

class IndexView(generic.ListView):

    template_name = './mainpage/index.html'
    context_object_name = 'content'

    def get_queryset(self):

        #object = Electronicparts.objects.filter(category = Categories.objects.first())

        #content[0] = object.order_by('part');

        if self.request.method == "POST":
            display_type = self.request.POST.get("display_type")
            print(display_type)  
        content[0] = Electronicparts.objects.all().order_by('part')
        return content




class SearchResultsView(generic.ListView):
    model = Electronicparts
    template_name = './mainpage/search.html'
    context_object_name = 'content'



    def get_queryset(self):

        query = self.request.GET.get("q")
        object_list = Electronicparts.objects.filter(
            Q(part__icontains=query) | Q(category__name__icontains=query) | Q(room_num__room__icontains=query) 
        )
        content[0] = object_list.order_by('part')
        return content 


def datasheet(request, part):
    
    filepath = os.path.join( "./datasheets",f'{part}')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')