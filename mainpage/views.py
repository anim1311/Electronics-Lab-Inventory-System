from sre_parse import CATEGORIES
from django.views import generic
from django.db.models import Q

from django.http import FileResponse, JsonResponse
import os
import json
from django.views.decorators.csrf import csrf_exempt

from collections import defaultdict
from .models import MAIN_LINKS, TOP_BAR_LINKS, Electronicparts, Storage, Categories
# Create your views here.
from django.conf import settings


top_bar_quick_links ={}
cart_items = defaultdict(list)

number_of_items_in_cart = 0

def refresh_top_bar_quick_links():
    for main_link in MAIN_LINKS.objects.all():
        top_bar_quick_links[main_link.main_name] = []
        for top_bar_link in TOP_BAR_LINKS.objects.filter(main=main_link):
            top_bar_quick_links[main_link.main_name].append(top_bar_link.top_bar_name)



content = [Electronicparts.objects.all(), top_bar_quick_links, Storage.objects.all(), Categories.objects.all(),number_of_items_in_cart]

class IndexView(generic.ListView):

    template_name = './mainpage/index.html'
    context_object_name = 'content'

    def get_queryset(self):

        #object = Electronicparts.objects.filter(category = Categories.objects.first())

        #content[0] = object.order_by('part');

        if self.request.method == "POST":
            pass
        content[0] = Electronicparts.objects.all().order_by('category')
        session_key = self.request.session.create()
        print(session_key)
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
        if self.request.method == "POST":
            pass
        content[0] = object_list.order_by('category')
        return content 


def datasheet(request, part):
    
    filepath = os.path.join( "./datasheets",f'{part}')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')





@csrf_exempt
def updateItem(requset):
    data = json.loads(requset.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    try:
        cart_items:list = list(set(json.loads(requset.COOKIES['cart'])))
        
    except:
        cart_items = []
    print("Before:",cart_items)

    cart_items.append(productId)
    content[4] = len(cart_items)
    
    print("After:",cart_items)
    response = JsonResponse("Item was added", safe=False)
    response.set_cookie("cart",json.dumps(cart_items,), max_age=5000);

    return response