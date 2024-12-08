from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import ContactDetail, PhoneNumber, ContactUs, Skill
from .forms import ContactUsForm

class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')


class AboutView(View):
    def get(self, request):
        skill = Skill.objects.all()
        return render(request, 'home/about.html', {'skill': skill})


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
