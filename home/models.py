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
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return f'{self.email} - {self.text}'


class YourProject(models.Model):
    project_name = models.CharField(max_length=100)
    project_number = models.IntegerField()

    def __str__(self):
        return f'{self.project_name}-{self.project_number}'

class YourSkill(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_percent = models.IntegerField(help_text='out of 100')

    def __str__(self):
        return f'{self.skill_name}-{self.skill_percent}'
class About(models.Model):
    description = models.TextField()
    project = models.ManyToManyField(YourProject)
    skill = models.ManyToManyField(YourSkill)

    def __str__(self):
        return f'{self.id} - this is your about'

