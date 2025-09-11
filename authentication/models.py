from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Department(models.Model):
    name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 10)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(null = True, blank = True)

class City(models.Model):
    name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column="id_department")

class User(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    mobile_phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)
    email = models.CharField(max_length = 50)
    password = models.TextField()
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(null = True, blank = True)
    id_city = models.ForeignKey(City, on_delete=models.CASCADE, db_column="id_city")


class Users(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20, blank = True)

