from django.contrib import admin
from .models import PhoneNumber, ContactDetail, ContactUs, YourProject, YourSkill, About, Service, Category

admin.site.register(ContactUs)


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1


class ContactDetailAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberInline]


class YourProjectInline(admin.TabularInline):
    model = YourProject
    extra = 1


class YourSkillInline(admin.TabularInline):
    model = YourSkill
    extra = 1


class AboutAdmin(admin.ModelAdmin):
    inlines = [YourProjectInline, YourSkillInline]


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class ServiceAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


admin.site.register(ContactDetail, ContactDetailAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)