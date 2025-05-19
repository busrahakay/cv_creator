from django.db import models

class CV(models.Model):
    TEMPLATE_CHOICES = [
        ('template1', 'Şablon 1'),
        ('template2', 'Şablon 2'),
        ('template3', 'Şablon 3'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='cv_photos/', null=True, blank=True)
    template = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, default='template1')
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
