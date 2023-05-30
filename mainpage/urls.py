from django.urls import path

from . import views

app_name = 'mainpage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("search/",views.SearchResultsView.as_view(), name="search"),
    path("datasheets/<str:part>", views.datasheet, name="datasheet"),
    path("update_item/", views.updateItem, name="update_item"),
    path("shoppingCart/", views.ShoppingBasketView.as_view(), name="shoppingCart"),
    path("download_pdf", views.download_pdf, name="download_pdf"),
]

