from django.db import models
from django.urls import reverse


class ContactDetail(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.email}'


class PhoneNumber(models.Model):
    contact = models.ForeignKey(ContactDetail, on_delete=models.CASCADE, related_name='phones')
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.phone


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return f'{self.email} - {self.text}'


class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return f'{self.id} - this is your about'


class YourProject(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=100)
    project_number = models.IntegerField()

    def __str__(self):
        return f'{self.project_name}-{self.project_number}'


class YourSkill(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)
    skill_percent = models.IntegerField(help_text='out of 100')

    def __str__(self):
        return f'{self.skill_name}-{self.skill_percent}'


class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/services/')
    description = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.title}-{self.price}'

class Category(models.Model):
    contact = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'
