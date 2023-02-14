from django.contrib import admin

from .models import MAIN_LINKS, TOP_BAR_LINKS, Electronicparts, Categories, Storage, Datasheet


class ElectronicpartsAdmin(admin.ModelAdmin):
    list_display = ('part', 'category', 'room_num')
    list_filter = ('category', 'room_num')
    search_fields = ('part',)


admin.site.register(MAIN_LINKS)
admin.site.register(TOP_BAR_LINKS)
admin.site.register(Storage)
admin.site.register(Electronicparts,ElectronicpartsAdmin)
admin.site.register(Categories)
admin.site.register(Datasheet)
