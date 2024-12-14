from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import ContactDetail, About
from .forms import ContactUsForm
from portfo.models import PortfolioDetail

class HomeView(View):
    def get(self, request, portfolio_id=None):
        portfo = PortfolioDetail.objects.order_by('-id')[:4]
        if portfolio_id:
            portfo.filter(id=portfolio_id)
        return render(request, 'home/index.html', {'portfo': portfo})

    def post(self, request, portfo_id):
        portfo = get_object_or_404(PortfolioDetail, id=portfo_id)
        return render(request, 'portfo/portfolio_detail.html', )

class AboutView(View):
    template_name = 'home/about.html'
    def get(self, request):
        about = get_object_or_404(About)
        return render(request, self.template_name, {'about': about})


class ContactView(View):
    form_class = ContactUsForm
    template_name = 'home/contact.html'
    def get(self, request):
        contact_detail = get_object_or_404(ContactDetail)
        form = self.form_class
        return render(request, self.template_name, {'contact': contact_detail, 'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:contact')
        return render(request, 'home/contact.html', {'form': form})
