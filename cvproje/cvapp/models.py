from django.db import models

class CV(models.Model):
    TEMPLATE_CHOICES = [
        ('template1', 'Modern'),
        ('template2', 'Dinamik'),
        ('template3', 'Yaratıcı'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='cv_photos/', null=True, blank=True)
    template = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, default='template1')
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
