from django.db import models


class PhoneNumber(models.Model):
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.phone
class ContactDetail(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField()
    location = models.CharField(max_length=255)
    phone = models.ManyToManyField(PhoneNumber)

    def __str__(self):
        return f'{self.email} - {self.phone}'

class ContactUs(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return f'{self.email} - {self.text}'
