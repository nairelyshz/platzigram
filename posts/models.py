from django.db import models
from django.contrib.auth.models import User
from profile import Profile
# Create your models here.
class Posts(models.Model):


    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey('users.profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modificated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} by @{}'.format(self.title,self.user.username)