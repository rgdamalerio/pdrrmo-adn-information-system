from django.db import models
from django.contrib.auth.admin import User
from django.core.validators import RegexValidator
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

  def __str__(self):
    return self.user.username

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
  if created:
    UserProfile.objects.create(user=instance)