from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import PortfolioDetail, Category, BlogDetail


class BlogView(View):
    def get(self, request, category_id=None):
        blog = BlogDetail.objects.all()
        categories = Category.objects.all()
        if category_id:
            category = Category.objects.get(id=category_id)
            blog = blog.filter(category=category)
        return render(request, 'portfo/blog.html', {'blog': blog, 'categories': categories})


class BlogDetailView(View):
    def get(self, request, blog_id=None):
        blog = get_object_or_404(BlogDetail, id=blog_id)
        return render(request, 'portfo/blog_detail.html', {'blog': blog})


class PortfolioView(View):
    def get(self, request, category_id=None):
        portfo = PortfolioDetail.objects.all()
        categories = Category.objects.all()
        if category_id:
            category = Category.objects.get(id=category_id)
            portfo = portfo.filter(category=category)
        return render(request, 'portfo/portfolio.html', {'portfo': portfo, 'categories': categories})


class PortfolioDetailView(View):
    def get(self, request, portfolio_id=None):
        portfolio = get_object_or_404(PortfolioDetail, id=portfolio_id)
        return render(request, 'portfo/portfolio_detail.html', {'portfolio': portfolio})
