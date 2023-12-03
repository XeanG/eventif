from django.contrib import admin
from .models import Contact_model

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    list_filter = ('created_at',)

admin.site.register(Contact_model, ContactAdmin)
