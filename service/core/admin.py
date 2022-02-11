from django.contrib import admin
from core.models import *
class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)
class AccountInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(AccountInfo, AccountInfoAdmin)
class BasicInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(BasicInfo, BasicInfoAdmin)
class ContactInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContactInfo, ContactInfoAdmin)
class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)
