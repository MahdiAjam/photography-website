from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('portfo:category', args=[self.id, ])


class PortfolioDetail(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='portfolios', null=True, blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
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

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.slug)
        super().save(*args, **kwargs)


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


class BlogDetail(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/blog/')
    tag = models.ManyToManyField(Category, related_name='tags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}-{self.tag}'

    def get_absolute_url(self):
        return reverse('portfo:blog detail', args=[self.id])


class ContentBlog(models.Model):
    blog_post = models.ForeignKey(BlogDetail, on_delete=models.CASCADE, related_name='blogs')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/blog/', null=True, blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return f'{self.order}'
