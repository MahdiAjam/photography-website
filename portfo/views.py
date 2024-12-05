from django.shortcuts import render
from django.views import View


class BlogView(View):
    def get(self, request):
        return render(request, 'portfo/blog.html')

class BlogDetailView(View):
    def get(self, request):
        return render(request, 'portfo/blog_detail.html')

class PortfolioView(View):
    def get(self, request):
        return render(request, 'portfo/portfolio.html')

class PortfolioDetailView(View):
    def get(self, request):
        return render(request, 'portfo/portfolio_detail.html')
