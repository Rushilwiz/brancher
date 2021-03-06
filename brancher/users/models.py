from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Influencer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.user.username}'s Profile"

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #
    #     img = Image.open(self.profile_pic.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.user.username}'s Profile"
