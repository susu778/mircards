# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Mircards(models.Model):
    Mature_id = models.CharField(db_column='Mature_id', primary_key=True,max_length=255, blank=True, null=False)  # Field name made lowercase.
    Accession = models.CharField(db_column='Accession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Sequence = models.CharField(db_column='Sequence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Seed_seq = models.CharField(db_column='Seed_seq', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mature_chrom = models.CharField(max_length=1000, blank=True, null=True)
    pre_mir = models.CharField(max_length=255, blank=True, null=True)
    evidence = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False  # 指定模型不由 Django 管理
        db_table = 'mircards' # 指定与模型对应的数据库表名




