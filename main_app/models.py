from email.policy import default
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    wrapper = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('packages_detail', kwargs={'package_id': self.id})

class Workflow(models.Model):
    TYPE = (
        ('ERR', 'Error'),
        ('WRK', 'Working'),
        ('FIN', 'Completed'),
    )

    class Meta:
        ordering = ('-date',)

    date = models.DateField('Work Date')
    type = models.CharField(max_length=3, choices=TYPE, default=TYPE[1][0])
    comment = models.CharField(max_length=150)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_type_display()} on {self.date}'