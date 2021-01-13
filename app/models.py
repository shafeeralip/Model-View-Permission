from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User


class Primeuser(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    class Meta:
        permissions=[('prime_member','prime_member')]

    