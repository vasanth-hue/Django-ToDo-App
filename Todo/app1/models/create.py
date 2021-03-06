from django.db import models

class Create(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    email = models

    def __str__(self):
        return self.title
    
    