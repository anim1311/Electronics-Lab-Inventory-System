from django.views import generic
from django.db.models import Q

from django.http import FileResponse, JsonResponse,HttpResponseBadRequest
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from collections import defaultdict
from .models import MAIN_LINKS, TOP_BAR_LINKS, Electronicparts, Storage, Categories

import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm 


top_bar_quick_links ={}
cart_items = defaultdict(list)

number_of_items_in_cart = len(cart_items)

def refresh_top_bar_quick_links():
    for main_link in MAIN_LINKS.objects.all():
        top_bar_quick_links[main_link.main_name] = []
        for top_bar_link in TOP_BAR_LINKS.objects.filter(main=main_link):
            top_bar_quick_links[main_link.main_name].append(top_bar_link.top_bar_name)



content = [Electronicparts.objects.all().order_by('category'), top_bar_quick_links, Storage.objects.all(), Categories.objects.all(),number_of_items_in_cart]

class IndexView(generic.ListView):
    model = Electronicparts
    template_name = './mainpage/index.html'
    context_object_name = 'content'
    content_class = content
    def get_queryset(self):

        #object = Electronicparts.objects.filter(category = Categories.objects.first())

        self.content_class[0] = Electronicparts.objects.all().order_by('category')[:50]

        if self.request.method == "POST":
            pass
        try:
            self.content_class[4] = len(set(json.loads(self.request.COOKIES['cart'])))
        except:
            self.content_class[4] = 0
        #print("len",self.content_class[4])
        return self.content_class
                

        




class SearchResultsView(generic.ListView):
    model = Electronicparts
    template_name = './mainpage/search.html'
    context_object_name = 'content'
    content_class = list(content)


    def get_queryset(self):

        query = self.request.GET.get("q")
        object_list = Electronicparts.objects.filter(
            Q(part__icontains=query) | Q(category__name__icontains=query) | Q(room_num__room__icontains=query) 
        )
        if self.request.method == "POST":
            pass
        self.content_class[0] = object_list.order_by('category')
        try:
            self.content_class[4] = len(set(json.loads(self.request.COOKIES['cart'])))
        except:
            self.content_class[4] = 0

        #print("len",self.content_class[4])
        return self.content_class

class ShoppingBasketView(generic.ListView):

    model = Electronicparts
    template_name = './mainpage/shoppingCart.html'
    context_object_name = 'content'
    content_class = content

    def get_queryset(self):

        if self.request.method == "POST":
            pass
        try:
            ids = list(set(json.loads(self.request.COOKIES['cart'])))
            self.content_class[0] = Electronicparts.objects.filter(id__in=ids).order_by('category')
        except:
            self.content_class[0] = 0

        return self.content_class
        





def datasheet(request,part):
    
    filepath = os.path.join( f"./datasheets/{part}")
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')





@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    #print('Action:', action)
    #print('Product:', productId)
    try:
        cart_items:list = list(set(json.loads(request.COOKIES['cart'])))
        
    except:
        cart_items = []
    #print("Before:",cart_items)

    if action == 'add':
        cart_items.append(productId)
    elif action == 'remove':
        cart_items.remove(productId)

    content[4] = len(cart_items)
    #print("After:",cart_items)
    
    response = JsonResponse("Item was added", safe=False)
    response.set_cookie("cart",json.dumps(cart_items,), max_age=5000);

    return response

def download_pdf(request):

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4,bottomup=0)
    
    textob = c.beginText()
    textob.setTextOrigin(1*cm, 1*cm)
    textob.setFont("Helvetica", 14)

    cart_items:list = list(set(json.loads(request.COOKIES['cart'])))
    parts = Electronicparts.objects.filter(id__in=cart_items).order_by('category')

    for part in parts:
        textob.textLine(f"Part Name: {part.part}")
        textob.textLine(f"Part Category: {part.category}")
        textob.textLine(f"Part Room: {part.room_num}")
        textob.textLine(f"Part Box Number: {part.box_num}")
        textob.textLine(f"Part Price: {part.price}")
        textob.textLine(f"Part Compartment: {part.compartment}")
        
        textob.textLine("="*50)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='shopping_cart.pdf')




    

from django.shortcuts import render


def error_404(request, exception):
    return render(request, 'mainpage/404.html')



def error_500(request, *args, **argv):
    return render(request, 'mainpage/500.html', status=500)

        
def error_403(request, exception):

        return render(request,'mainpage/403.html')

def error_400(request,  exception):
        return HttpResponseBadRequest('Bad Request!')
