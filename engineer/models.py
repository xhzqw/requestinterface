from django.db import models

# Create your models here.
class Engineer(models.Model):
    GENDER_CHOICES = [
        ('M', 'male'),
        ('F', 'female'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # avatar = models.ImageField(upload_to='avatars/')
    phone_number = models.CharField(max_length=15, unique=True)
    is_available = models.BooleanField(default=True)
    work_order_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name