from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import ContactDetail, PhoneNumber

class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'home/about.html')


class ContactView(View):
    template_name = 'home/contact.html'

    def get(self, request):
        contact_detail = get_object_or_404(ContactDetail)
        return render(request, self.template_name, {'contact': contact_detail})

