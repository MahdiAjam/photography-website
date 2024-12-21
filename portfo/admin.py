from django.contrib import admin
from .models import PortfolioDetail, PortfolioImage, Category, BlogDetail, ContentBlog, Comment

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

class PortfolioDetailAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PortfolioImageInline]

class ContentBlogInline(admin.TabularInline):
    model = ContentBlog
    extra = 2

class BlogDetailAdmin(admin.ModelAdmin):
    inlines = [ContentBlogInline]


admin.site.register(PortfolioDetail, PortfolioDetailAdmin)
admin.site.register(Category)
admin.site.register(BlogDetail, BlogDetailAdmin)
admin.site.register(Comment)