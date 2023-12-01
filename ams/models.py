# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=255)
    user_psw = models.CharField(max_length=20)
    user_grade = models.CharField(max_length=20, blank=True, null=True)
    user_no = models.CharField(db_column='user_No', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
