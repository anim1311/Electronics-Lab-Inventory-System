import datetime

from django.db import models
from django.utils import timezone


class MAIN_LINKS(models.Model):
    
    main_name = models.CharField(max_length=200)

    def __str__(self):
        return self.main_name
    def reload(self):
        new_self = self.__class__.objects.get(pk=self.pk)
        self.__dict__.update(new_self.__dict__)

class TOP_BAR_LINKS(models.Model):

    main = models.ForeignKey(MAIN_LINKS, on_delete=models.CASCADE)
    top_bar_name = models.CharField(max_length=200)

    def __str__(self):
        return self.top_bar_name
    
    
class Storage(models.Model):
    room = models.CharField(primary_key=True, max_length=32, db_collation='utf8mb3_general_ci')
    longname = models.CharField(max_length=32, db_collation='utf8mb3_general_ci')
    shortname = models.CharField(max_length=32, db_collation='utf8mb3_general_ci')
    responsible_person = models.CharField(max_length=32)
    title_en = models.CharField(max_length=32, db_collation='utf8mb3_general_ci')
    title_de = models.CharField(max_length=32, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'storage'
    
    def __str__(self):
        return self.room


class Categories(models.Model):
    name = models.CharField(primary_key=True, max_length=32, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.name

class Electronicparts(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='category')
    part = models.CharField(max_length=256, db_collation='utf8mb3_general_ci')
    datasheet = models.CharField(max_length=32, db_collation='utf8mb3_general_ci', blank=True, null=True)
    room_num = models.ForeignKey('Storage', models.DO_NOTHING, db_column='room_num')
    box_num = models.IntegerField(blank=True, null=True)
    reichelt_name = models.CharField(max_length=32, db_collation='utf8mb3_general_ci', blank=True, null=True)
    reichelt_num = models.CharField(max_length=32, db_collation='utf8mb3_general_ci', blank=True, null=True)
    link_reichelt = models.CharField(max_length=128, db_collation='utf8mb3_general_ci', blank=True, null=True)
    link_conrad = models.CharField(max_length=128, db_collation='utf8mb3_general_ci', blank=True, null=True)
    link_voelkner = models.CharField(max_length=128, db_collation='utf8mb3_general_ci', blank=True, null=True)
    link_farnell = models.CharField(max_length=128, db_collation='utf8mb3_general_ci', blank=True, null=True)
    link_rs = models.CharField(max_length=128, db_collation='utf8mb3_general_ci', blank=True, null=True)
    link_mouser = models.CharField(max_length=128, db_collation='utf8mb3_general_ci', blank=True, null=True)
    link_digikey = models.CharField(max_length=128, db_collation='utf8mb3_general_ci', blank=True, null=True)
    link_other = models.CharField(max_length=128, db_collation='utf8mb3_general_ci', blank=True, null=True)
    remainder = models.IntegerField()
    available = models.IntegerField()
    date_added = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    compartment = models.CharField(max_length=32, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'electronicparts'
    
    def __str__(self):
        return self.part
    