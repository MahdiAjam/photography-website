from django.contrib import admin
from .models import PhoneNumber, ContactDetail, ContactUs, Skill

admin.site.register(PhoneNumber)
admin.site.register(ContactDetail)
admin.site.register(ContactUs)
admin.site.register(Skill)
