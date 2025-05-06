from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Profile(models.Model):
    
    BG_CHOICES = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        
    )
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"), max_length=100)
    bg_color = models.CharField(_("Background Color"), max_length=50, choices=BG_CHOICES)
    
    
    def __str__(self):
        return self.name
    

class Link(models.Model):
    text = models.TextField(_("Text"), max_length=100)
    url = models.URLField(_("URL"), max_length=200)
    profile = models.ForeignKey(Profile, related_name="link", on_delete=models.CASCADE)