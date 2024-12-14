from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import PortfolioDetail

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
    def get(self, request, portfolio_id):
        portfolio = get_object_or_404(PortfolioDetail, id=portfolio_id)
        return render(request, 'portfo/portfolio_detail.html', {'portfolio': portfolio})
