from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    qns_text = models.CharField(max_length=2000)
    post_date = models.DateTimeField("date published")
    def __str__(self):
        return self.qns_text
    def was_published_recently(self):
        return self.post_date >= timezone.now() - timezone.timedelta(days=1)
    @property
    def total_votes(self):
        return sum(choice.votes for choice in self.choice_set.all())

    
class Choice(models.Model):
    qns = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text =  models.CharField(max_length = 2000)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text