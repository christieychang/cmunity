from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserData(models.Model):
    score = models.IntegerField(default=0)
    andrewID = models.CharField(max_length=20, default="")

# def popUpImage(self, other):
#     #Ready button
#     index = random.randint(0,5)
#     image = self.imageList[index]

#     #Small
#     self.guess = 
#     other.options = 