# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employee(models.Model):
    employeeid = models.IntegerField(db_column='employeeID', primary_key=True)  # Field name made lowercase.
    medicare = models.CharField(unique=True, max_length=12)
    firstname = models.CharField(db_column='firstName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='dateOfBirth', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    postal = models.CharField(max_length=7, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    citzenship = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Employee'


class Employeerole(models.Model):
    occupationid = models.OneToOneField('Occupation', models.DO_NOTHING, db_column='occupationID', primary_key=True)  # Field name made lowercase. The composite primary key (occupationID, employeeID) found, that is not supported. The first column is selected.
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employeeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeeRole'
        unique_together = (('occupationid', 'employeeid'),)


class Facility(models.Model):
    facilityid = models.AutoField(db_column='facilityID', primary_key=True)  # Field name made lowercase.
    facilityname = models.CharField(db_column='facilityName', max_length=75, blank=True, null=True)  # Field name made lowercase.
    facilitywebaddress = models.CharField(db_column='facilityWebAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    facilitytype = models.CharField(db_column='facilityType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    facilityphone = models.CharField(db_column='facilityPhone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    facilityaddress = models.CharField(db_column='facilityAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    facilitypostalcode = models.CharField(db_column='facilityPostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Facility'


class Infected(models.Model):
    infectionnumber = models.IntegerField(db_column='infectionNumber', primary_key=True)  # Field name made lowercase. The composite primary key (infectionNumber, employeeID) found, that is not supported. The first column is selected.
    infectiondate = models.DateField(db_column='infectionDate', blank=True, null=True)  # Field name made lowercase.
    infectiontype = models.CharField(db_column='infectionType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employeeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Infected'
        unique_together = (('infectionnumber', 'employeeid'),)


class Occupation(models.Model):
    occupationid = models.IntegerField(db_column='occupationID', primary_key=True)  # Field name made lowercase.
    occupationname = models.CharField(db_column='occupationName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Occupation'


class Postalcode(models.Model):
    postalcode = models.CharField(db_column='postalCode', primary_key=True, max_length=30)  # Field name made lowercase.
    province = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PostalCode'


class Received(models.Model):
    vaccineid = models.ForeignKey('Vaccine', models.DO_NOTHING, db_column='vaccineID', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.OneToOneField(Employee, models.DO_NOTHING, db_column='employeeID', primary_key=True)  # Field name made lowercase. The composite primary key (employeeID, doseNum) found, that is not supported. The first column is selected.
    dosenum = models.IntegerField(db_column='doseNum')  # Field name made lowercase.
    datereceived = models.DateField(db_column='dateReceived', blank=True, null=True)  # Field name made lowercase.
    facilityid = models.ForeignKey(Facility, models.DO_NOTHING, db_column='facilityID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Received'
        unique_together = (('employeeid', 'dosenum'),)


class Schedules(models.Model):
    scheduleid = models.IntegerField(db_column='scheduleID', primary_key=True)  # Field name made lowercase.
    facilityid = models.ForeignKey(Facility, models.DO_NOTHING, db_column='facilityID', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employeeID', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    scheduledate = models.DateField(db_column='scheduleDate', blank=True, null=True)  # Field name made lowercase.
    occupationname = models.CharField(db_column='occupationName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedules'


class Vaccine(models.Model):
    vaccineid = models.IntegerField(db_column='vaccineID', primary_key=True)  # Field name made lowercase.
    vaccinename = models.CharField(db_column='vaccineName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vaccine'


class Workat(models.Model):
    facilityid = models.ForeignKey(Facility, models.DO_NOTHING, db_column='facilityID')  # Field name made lowercase.
    employeeid = models.OneToOneField(Employee, models.DO_NOTHING, db_column='employeeID', primary_key=True)  # Field name made lowercase. The composite primary key (employeeID, facilityID, startdate) found, that is not supported. The first column is selected.
    startdate = models.DateField()
    enddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WorkAt'
        unique_together = (('employeeid', 'facilityid', 'startdate'),)


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
