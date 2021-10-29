from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    question = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='questions', blank=True)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def likes_count(self):
        return self.likes.count()

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='answers', blank=True)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return f"Answer: {self.question}-{self.user}"

    @property
    def likes_count(self):
        return self.likes.count()