from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

class PortfolioDetail(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    video = models.FileField(upload_to='video/portfolio', null=True, blank=True)
    video_description = models.TextField(null=True, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}-{self.category}'

    def get_absolute_url(self):
        return reverse('portfo:portfolio detail', args=[self.id])


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(PortfolioDetail, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/portfolio/')

    def __str__(self):
        return f'Image for {self.portfolio.title}'

@receiver(post_delete, sender=PortfolioImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

@receiver(post_delete, sender=PortfolioDetail)
def delete_video_file(sender, instance, **kwargs):
    if instance.video:
        instance.video.delete(save=False)
