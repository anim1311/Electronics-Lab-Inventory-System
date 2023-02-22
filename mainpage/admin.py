from django.contrib import admin
from django.core.mail import send_mail

from .models import MAIN_LINKS, TOP_BAR_LINKS, Electronicparts, Categories, Storage, Datasheet,Mail

@admin.action(description='Get a buy list sent to email')
def sendMail( modeladmin, queryset,  items):
    mail_list = []
    for mail in Mail.objects.all():
        if mail.send_to_this:
            mail_list.append(mail.mail)
    
    subject = "Low on stock - Automated message"
    message = "\nHello, \n\nThis is an automated message from the electronics inventory app. \n\nThe following items are low on stock and need to be ordered: \n\n"
    for item in items:
        message += "Part: " + item.part + " - Category: " + item.category.name + " - Room: " + item.room_num.room + " - Link to Buy: \n" 
        if item.link_mouser:
            message += item.link_mouser+"\n"
                             
        if item.link_reichelt :
            message += item.link_reichelt+"\n"
        
        if item.link_conrad:
            message += item.link_conrad+"\n"
        

        if item.link_voelkner:
            message += item.link_voelkner+"\n"
        
        if item.link_farnell:
            message += item.link_farnell+"\n"
        
        if item.link_rs:
            message += item.link_rs+"\n"
        
        if item.link_digikey: 
            message += item.link_digikey+"\n"
        
        if item.link_other:
            message += item.link_other+"\n"
        
        if  not item.link_other and  not item.link_digikey and not item.link_rs and not item.link_farnell and not item.link_voelkner and not item.link_conrad  and not item.link_reichelt and not item.link_mouser:
            message += "No link available\n"
        
        message += "\n"
        
        send_mail(
            subject = subject,
            message = message,
            from_email = "anirudhm1311@gmail.com",
            recipient_list = mail_list,
            fail_silently=False
        )
                             
    
    
    


class ElectronicpartsAdmin(admin.ModelAdmin):
    list_display = ('part', 'category', 'room_num')
    list_filter = ('category', 'room_num')
    search_fields = ('part',)
    actions = [sendMail]

admin.site.register(MAIN_LINKS)
admin.site.register(TOP_BAR_LINKS)
admin.site.register(Storage)
admin.site.register(Electronicparts,ElectronicpartsAdmin)
admin.site.register(Categories)
admin.site.register(Datasheet)
admin.site.register(Mail)




