from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import PortfolioDetail, Category, BlogDetail, Comment
from .forms import CommentForm, SearchForm


class BlogView(View):
    form_class = SearchForm

    def get(self, request, category_id=None):
        blog = BlogDetail.objects.all()
        categories = Category.objects.all()

        if request.GET.get('search'):
            blog = blog.filter(title__contains=request.GET['search'])

        if category_id:
            category = Category.objects.get(id=category_id)
            blog = blog.filter(category=category)

        return render(request, 'portfo/blog.html', {'blog': blog, 'categories': categories,
                                                    'form': self.form_class})


class BlogDetailView(View):
    template_name = 'portfo/blog_detail.html'
    form_class = CommentForm

    def get(self, request, blog_id=None):
        blog = get_object_or_404(BlogDetail, id=blog_id)
        form = self.form_class
        comment = Comment.objects.filter(blog_post_id=blog_id)
        return render(request, self.template_name, {'blog': blog, 'form': form, 'comment': comment})

    def post(self, request, blog_id=None):
        blog = get_object_or_404(BlogDetail, id=blog_id)
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog_post = blog
            new_comment.save()
            return redirect('portfo:blog detail', blog_id=blog_id)
        comment = Comment.objects.filter(blog_post_id=blog_id)
        return render(request, self.template_name, {'form': form, 'blog': blog, 'comment': comment})


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
