from django.urls import path
from . import views

app_name = 'portfo'
urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/sample/', views.BlogDetailView.as_view(), name='blog detail'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio/sample/', views.PortfolioDetailView.as_view(), name='portfolio detail'),
]
