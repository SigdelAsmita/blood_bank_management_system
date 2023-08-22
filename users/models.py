from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    national_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    blood_group = models.TextField()  # This field type is a guess.
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to='profile_pics')

    class Meta:
        db_table = 'person'
    
    def __str__(self):
        return f'{self.user.username} Profile'


class Relationship(models.Model):
    person1 = models.OneToOneField(Person, models.DO_NOTHING, primary_key=True)  # The composite primary key (person1_id, person2_id) found, that is not supported. The first column is selected.
    person2 = models.ForeignKey(Person, models.DO_NOTHING, related_name='relationship_person2_set')
    relation = models.CharField(blank=True, null=True,max_length=50)

    class Meta:
        db_table = 'relationship'
        unique_together = (('person1', 'person2'),)

class BloodBank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    blood_bank_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50,blank=True, null=True)
    website = models.URLField(max_length=100, null=True, blank=True)
    image=models.ImageField(upload_to='')
    class Meta:
        db_table = 'blood_bank'

class Blood(models.Model):
    blood_id = models.BigIntegerField(primary_key=True)
    bank = models.ForeignKey('BloodBank', models.DO_NOTHING, blank=True, null=True)
    donor = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    donation_date = models.DateField()
    blood_group = models.TextField()  # This field type is a guess.
    quantity = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)

    class Meta:
        db_table = 'blood'

class Reception(models.Model):
    receiver = models.OneToOneField(Person, models.DO_NOTHING, primary_key=True)  # The composite primary key (receiver_id, blood_id) found, that is not supported. The first column is selected.
    blood = models.ForeignKey(Blood, models.DO_NOTHING)
    reception_id = models.DateField()
    blood_group = models.TextField()  # This field type is a guess.
    quantity = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)

    class Meta:
        db_table = 'reception'
        unique_together = (('receiver', 'blood'),)

class Diseases(models.Model):
    national = models.OneToOneField('Person', models.DO_NOTHING, primary_key=True)  # The composite primary key (national_id, disease_name) found, that is not supported. The first column is selected.
    disease_name = models.CharField(max_length=20)
    from_field = models.DateField(db_column='from_date', blank=True, null=True)  # Field renamed because it ended with '_'.
    to_field = models.DateField(db_column='to_date', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        db_table = 'diseases'
        unique_together = (('national', 'disease_name'),)

class Immunizations(models.Model):
    national = models.OneToOneField('Person', models.DO_NOTHING, primary_key=True)  # The composite primary key (national_id, vaccine_name) found, that is not supported. The first column is selected.
    vaccine_name = models.CharField(max_length=20)
    date_of_vaccination = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'immunizations'
        unique_together = (('national', 'vaccine_name'),)

class Surgeries(models.Model):
    national = models.OneToOneField('Person', models.DO_NOTHING, primary_key=True)  # The composite primary key (national_id, surgery_name) found, that is not supported. The first column is selected.
    surgery_name = models.CharField(max_length=30)
    part_of_body = models.CharField(max_length=20, blank=True, null=True)
    recovery_time = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'surgeries'
        unique_together = (('national', 'surgery_name'),)


class BankPost(models.Model):
    post_id = models.AutoField(primary_key = True)
    author = models.ForeignKey('BloodBank',on_delete=models.CASCADE)
    date_posted = models.DateField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    class Meta:
        db_table='bank_post'
  
    def __str__(self):
        return self.title
    

