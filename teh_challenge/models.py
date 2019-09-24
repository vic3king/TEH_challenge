from django.db import models

class UserReg(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    job_position = models.CharField(max_length=100)

    def __str__(self):
      return self.first_name