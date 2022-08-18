from django.db import models

# Create your models here.
class MyModel(models.Model):
    # Columns
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
         return self.name
    class Meta:
        db_table = 'my_users_table'
