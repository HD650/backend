# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    area_name = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'area'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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


class AuthUser(models.Model):
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

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Company(models.Model):
    company_name = models.CharField(unique=True, max_length=128)
    company_description = models.CharField(max_length=4096, blank=True, null=True)
    company_location = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    fax = models.CharField(max_length=45, blank=True, null=True)
    county = models.CharField(max_length=45, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    company_type = models.CharField(max_length=128, blank=True, null=True)
    year_founded = models.CharField(max_length=45, blank=True, null=True)
    employment_in_nc = models.CharField(max_length=45, blank=True, null=True)
    us_headquarters = models.CharField(max_length=128, blank=True, null=True)
    global_headquarters = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class CompanyAreaRelationship(models.Model):
    company_id = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_area_relationship'


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


class Pma(models.Model):
    pmanumber = models.CharField(db_column='PMANUMBER', max_length=256, blank=True, null=True)  # Field name made lowercase.
    supplementnumber = models.CharField(db_column='SUPPLEMENTNUMBER', max_length=256, blank=True, null=True)  # Field name made lowercase.
    applicant = models.CharField(db_column='APPLICANT', max_length=256, blank=True, null=True)  # Field name made lowercase.
    street_1 = models.CharField(db_column='STREET_1', max_length=256, blank=True, null=True)  # Field name made lowercase.
    street_2 = models.CharField(db_column='STREET_2', max_length=256, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=256, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=256, blank=True, null=True)  # Field name made lowercase.
    zip_ext = models.CharField(db_column='ZIP_EXT', max_length=256, blank=True, null=True)  # Field name made lowercase.
    genericname = models.CharField(db_column='GENERICNAME', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tradename = models.CharField(db_column='TRADENAME', max_length=256, blank=True, null=True)  # Field name made lowercase.
    productcode = models.CharField(db_column='PRODUCTCODE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    advisorycommittee = models.CharField(db_column='ADVISORYCOMMITTEE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    supplementtype = models.CharField(db_column='SUPPLEMENTTYPE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    supplementreason = models.CharField(db_column='SUPPLEMENTREASON', max_length=256, blank=True, null=True)  # Field name made lowercase.
    reviewgrantedyn = models.CharField(db_column='REVIEWGRANTEDYN', max_length=256, blank=True, null=True)  # Field name made lowercase.
    datereceived = models.DateField(db_column='DATERECEIVED', blank=True, null=True)  # Field name made lowercase.
    decisiondate = models.DateField(db_column='DECISIONDATE', blank=True, null=True)  # Field name made lowercase.
    docketnumber = models.CharField(db_column='DOCKETNUMBER', max_length=256, blank=True, null=True)  # Field name made lowercase.
    fedregnoticedate = models.DateField(db_column='FEDREGNOTICEDATE', blank=True, null=True)  # Field name made lowercase.
    decisioncode = models.CharField(db_column='DECISIONCODE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    aostatement = models.CharField(db_column='AOSTATEMENT', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pma'


class PmnSince1996(models.Model):
    knumber = models.CharField(db_column='KNUMBER', max_length=256, blank=True, null=True)  # Field name made lowercase.
    applicant = models.CharField(db_column='APPLICANT', max_length=256, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='CONTACT', max_length=256, blank=True, null=True)  # Field name made lowercase.
    street1 = models.CharField(db_column='STREET1', max_length=256, blank=True, null=True)  # Field name made lowercase.
    street2 = models.CharField(db_column='STREET2', max_length=256, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=256, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    country_code = models.CharField(db_column='COUNTRY_CODE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=256, blank=True, null=True)  # Field name made lowercase.
    postal_code = models.CharField(db_column='POSTAL_CODE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    datereceived = models.DateField(db_column='DATERECEIVED', blank=True, null=True)  # Field name made lowercase.
    decisiondate = models.DateField(db_column='DECISIONDATE', blank=True, null=True)  # Field name made lowercase.
    decision = models.CharField(db_column='DECISION', max_length=256, blank=True, null=True)  # Field name made lowercase.
    reviewadvisecomm = models.CharField(db_column='REVIEWADVISECOMM', max_length=256, blank=True, null=True)  # Field name made lowercase.
    productcode = models.CharField(db_column='PRODUCTCODE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    stateorsumm = models.CharField(db_column='STATEORSUMM', max_length=256, blank=True, null=True)  # Field name made lowercase.
    classadvisecomm = models.CharField(db_column='CLASSADVISECOMM', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sspindicator = models.CharField(db_column='SSPINDICATOR', max_length=256, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    thirdparty = models.CharField(db_column='THIRDPARTY', max_length=256, blank=True, null=True)  # Field name made lowercase.
    expeditedreview = models.CharField(db_column='EXPEDITEDREVIEW', max_length=256, blank=True, null=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='DEVICENAME', max_length=512, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pmn_since_1996'


class Sbirsttr(models.Model):
    company_name = models.CharField(db_column='Company_Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    duns = models.CharField(db_column='DUNS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    num_of_awards = models.IntegerField(db_column='Num_of_Awards', blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=256, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=256, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=128, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=45, blank=True, null=True)  # Field name made lowercase.
    company_website = models.CharField(db_column='Company_Website', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sbirsttr'
