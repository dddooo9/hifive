from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MinLengthValidator

class Camera(models.Model):
    date = models.DateField(null=True)
    basic_img = models.TextField(null=True)
    outline_img = models.TextField(null=True)
    joint_img = models.TextField(null=True)
    outline_area = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    device_pw = models.CharField(max_length=4, validators=[MinLengthValidator(4)], default="0000")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()