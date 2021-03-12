from django.db import models

# Create your models here.

class comment(models.Model):
    email=models.EmailField(null=False)
    email2=models.EmailField(null=False)
    content=models.TextField(max_length=120)
    num=models.IntegerField(null=True)

    def __str__(self):
        return self.email   