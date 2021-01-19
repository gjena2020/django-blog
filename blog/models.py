from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self, *args, **kwargs):
        return '/blog/detail/{}'.format(self.id)
    
    
    def __str__(self):
        return self.title
