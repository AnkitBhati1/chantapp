from django.db import models
from django.contrib.auth.models import User

# Create your models here.  

class chatRoom(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User, related_name='chatroom')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class message(models.Model):
    chatroom = models.ForeignKey(chatRoom, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content