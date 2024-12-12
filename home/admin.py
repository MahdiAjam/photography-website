from django.contrib import admin
from .models import PhoneNumber, ContactDetail, ContactUs, YourProject, YourSkill, About

admin.site.register(PhoneNumber)
admin.site.register(ContactDetail)
admin.site.register(ContactUs)
admin.site.register(YourProject)
admin.site.register(YourSkill)
admin.site.register(About)
