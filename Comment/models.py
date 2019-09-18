from django.db import models
from django.conf import settings
from Food.models import Food

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='user_comments',on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    food = models.ForeignKey(Food,related_name='comments',on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.user.username
