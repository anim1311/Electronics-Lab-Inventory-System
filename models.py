# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    name = models.CharField(primary_key=True, max_length=32, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'categories'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class MainpageMainLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    main_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'mainpage_main_links'


class MainpageStorage(models.Model):
    id = models.BigAutoField(primary_key=True)
    room = models.CharField(max_length=200)
    longname = models.CharField(max_length=200)
    shortname = models.CharField(max_length=200)
    responsible_person = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_de = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'mainpage_storage'


class MainpageTopBarLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    top_bar_name = models.CharField(max_length=200)
    main = models.ForeignKey(MainpageMainLinks, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mainpage_top_bar_links'


class PollsChoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


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
