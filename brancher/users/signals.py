from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Influencer, Company

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if (isInfluencer(instance)):
            Influencer.objects.create(user=instance)

        if (isCompany(instance)):
            Company.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if (isInfluencer(instance)):
        instance.influencer.save()

    if (isCompany(instance)):
        instance.company.save()


def isInfluencer(user):
    return user.groups.filter(name='Influencer').exists()

def isCompany(user):
    return user.groups.filter(name='Company').exists()
