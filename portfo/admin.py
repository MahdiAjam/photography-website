from django.contrib import admin
from .models import PortfolioDetail, PortfolioImage

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

class PortfolioDetailAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline]


admin.site.register(PortfolioDetail, PortfolioDetailAdmin)
