from django.contrib import admin
from mymessages.models import Message


class MyMessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'timestamp')


admin.site.register(Message, MyMessageAdmin)
