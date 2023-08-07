from django.db import models

class User(models.Model):
    User_Id = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=100)
    Family_Name = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=100)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Rol = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = "[B2B].[TCUser]"