from django.db import models

# Create your models here.

class Record(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True,null=True)
    type = models.IntegerField(choices=[(0,"収入"),(1,"支出")])
    amount = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.title