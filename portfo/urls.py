from django.urls import path
from . import views

app_name = 'portfo'
urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/sample/', views.BlogDetailView.as_view(), name='blog detail'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<int:portfolio_id>/', views.PortfolioDetailView.as_view(), name='portfolio detail'),
    path('category/<int:category_id>/', views.PortfolioView.as_view(), name='category'),

]
