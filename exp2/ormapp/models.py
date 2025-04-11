from django.db import models

from django.contrib import admin
class Movies(models.Model):
    userid=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=30)
    mobileno=models.IntegerField()
    mailid=models.EmailField()
    moviename=models.CharField(max_length=50)
    noofseats=models.IntegerField()
    date=models.DateField()

class MoviesAdmin(admin.ModelAdmin):
    list_display=('username','moviename','noofseats','mailid')
