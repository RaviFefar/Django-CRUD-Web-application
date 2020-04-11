from django.db import models

class Stud(models.Model):
        name = models.CharField(max_length = 50 )
        email = models.EmailField(blank = True )
        number = models.IntegerField()
        hobbies = models.CharField(blank = True, max_length =255 )
        gender = models.CharField(blank = True, max_length =50 )
        education = models.CharField(blank = True, max_length =50 )
        image = models.FileField(upload_to='student_image',blank = True)
        age = models.CharField(blank = True,max_length =50 )

        class Meta:
            db_table = "student"
# Create your models here.
