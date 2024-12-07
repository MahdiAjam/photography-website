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
<<<<<<< HEAD
    phone = models.ManyToManyField(PhoneNumber)
=======
    phone = models.ManyToManyField(PhoneNumber, related_name='contact_detail')
>>>>>>> 8770e349b65ad340c7f3513d2b97f21b5782f2cf

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
