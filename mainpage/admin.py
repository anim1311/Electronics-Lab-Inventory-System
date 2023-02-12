from django.contrib import admin

from .models import MAIN_LINKS, TOP_BAR_LINKS, Electronicparts, Categories, Storage

admin.site.register(MAIN_LINKS)
admin.site.register(TOP_BAR_LINKS)
admin.site.register(Storage)
admin.site.register(Electronicparts)
admin.site.register(Categories)