from django.contrib import admin
from .models import Contact, UserContact


admin.site.register(Contact)
admin.site.register(UserContact)