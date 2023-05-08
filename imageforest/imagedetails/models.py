from django.db import models

class image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100,)
    image = models.ImageField(upload_to='images/',null=True)

    class Meta:
        db_table="image"
        
    def __str__(self):
        return self.title