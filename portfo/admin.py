from django.contrib import admin
from .models import PortfolioDetail, PortfolioImage, Category

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

class PortfolioDetailAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PortfolioImageInline]


admin.site.register(PortfolioDetail, PortfolioDetailAdmin)
admin.site.register(Category)