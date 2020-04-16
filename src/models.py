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


class Book(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=50)  # Field name made lowercase.
    book_title = models.CharField(max_length=50, blank=True, null=True)
    book_author = models.CharField(max_length=50, blank=True, null=True)
    book_publisher = models.CharField(max_length=50, blank=True, null=True)
    book_subject = models.CharField(max_length=50, blank=True, null=True)
    date_of_publication = models.DateField(blank=True, null=True)
    msrp = models.FloatField(db_column='MSRP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'


class Copy(models.Model):
    item = models.OneToOneField('Media', models.DO_NOTHING, db_column='item_ID', primary_key=True)  # Field name made lowercase.
    copy_id = models.IntegerField(db_column='copy_ID')  # Field name made lowercase.
    loaned = models.IntegerField()
    damaged = models.IntegerField()
    lost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'copy'
        unique_together = (('item', 'copy_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('SignUpUser', models.DO_NOTHING)

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


class Fine(models.Model):
    fine_id = models.IntegerField(db_column='fine_ID', primary_key=True)  # Field name made lowercase.
    loan = models.ForeignKey('Loan', models.DO_NOTHING, db_column='loan_ID')  # Field name made lowercase.
    user = models.ForeignKey('SignUpUser', models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.
    amount_due = models.FloatField()
    paid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fine'


class Laptop(models.Model):
    lap_model = models.CharField(primary_key=True, max_length=50)
    lap_os = models.CharField(db_column='lap_OS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date_of_manufacture = models.DateField(blank=True, null=True)
    msrp = models.FloatField(db_column='MSRP', blank=True, null=True)  # Field name made lowercase.
    lap_manufacturer = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laptop'


class Loan(models.Model):
    loan_id = models.IntegerField(db_column='loan_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('SignUpUser', models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.
    item = models.ForeignKey('Media', models.DO_NOTHING, db_column='item_ID')  # Field name made lowercase.
    item_copy_id = models.IntegerField(db_column='item_copy_ID')  # Field name made lowercase.
    borrow_date = models.DateField(blank=True, null=True)
    return_due_date = models.DateField(blank=True, null=True)
    overdue_date_num = models.IntegerField(blank=True, null=True)
    damaged = models.IntegerField(blank=True, null=True)
    lost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan'


class Media(models.Model):
    media_id = models.CharField(db_column='media_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    media_title = models.CharField(max_length=50, blank=True, null=True)
    media_author = models.CharField(max_length=30, blank=True, null=True)
    media_publisher = models.CharField(max_length=60, blank=True, null=True)
    media_subject = models.CharField(max_length=25, blank=True, null=True)
    media_date_publication = models.DateField(blank=True, null=True)
    msrp = models.FloatField(db_column='MSRP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'media'


class Reserve(models.Model):
    reservation_id = models.IntegerField(db_column='reservation_ID', primary_key=True)  # Field name made lowercase.
    reservation_date = models.DateField()
    user = models.ForeignKey('SignUpUser', models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.
    item = models.ForeignKey(Media, models.DO_NOTHING, db_column='item_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reserve'


class SignUpUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    user_type = models.ForeignKey('UserTypeInfo', models.DO_NOTHING, db_column='user_type')

    class Meta:
        managed = False
        db_table = 'sign_up_user'


class SignUpUserGroups(models.Model):
    user = models.ForeignKey(SignUpUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sign_up_user_groups'
        unique_together = (('user', 'group'),)


class SignUpUserUserPermissions(models.Model):
    user = models.ForeignKey(SignUpUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sign_up_user_user_permissions'
        unique_together = (('user', 'permission'),)


class UserTypeInfo(models.Model):
    user_type_id = models.CharField(primary_key=True, max_length=5)
    user_type = models.CharField(max_length=20)
    borrow_time_limit = models.IntegerField(blank=True, null=True)
    borrow_amount_limit = models.IntegerField(blank=True, null=True)
    reservation_amount_limit = models.IntegerField(blank=True, null=True)
    overdue_fine_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_type_info'
