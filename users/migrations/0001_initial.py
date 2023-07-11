# Generated by Django 4.2.3 on 2023-07-11 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('bank_id', models.AutoField(primary_key=True, serialize=False)),
                ('blood_bank_name', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, null=True)),
            ],
            options={
                'db_table': 'blood_bank',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('national_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField()),
                ('blood_group', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('blood_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('donation_date', models.DateField()),
                ('blood_group', models.TextField()),
                ('quantity', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.bloodbank')),
                ('donor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.person')),
            ],
            options={
                'db_table': 'blood',
            },
        ),
        migrations.CreateModel(
            name='BankPost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_posted', models.DateField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.bloodbank')),
            ],
            options={
                'db_table': 'bank_post',
            },
        ),
        migrations.CreateModel(
            name='Surgeries',
            fields=[
                ('national', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.person')),
                ('surgery_name', models.CharField(max_length=30)),
                ('part_of_body', models.CharField(blank=True, max_length=20, null=True)),
                ('recovery_time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'surgeries',
                'unique_together': {('national', 'surgery_name')},
            },
        ),
        migrations.CreateModel(
            name='Immunizations',
            fields=[
                ('national', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.person')),
                ('vaccine_name', models.CharField(max_length=20)),
                ('date_of_vaccination', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'immunizations',
                'unique_together': {('national', 'vaccine_name')},
            },
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('national', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.person')),
                ('disease_name', models.CharField(max_length=20)),
                ('from_field', models.DateField(blank=True, db_column='from_date', null=True)),
                ('to_field', models.DateField(blank=True, db_column='to_date', null=True)),
            ],
            options={
                'db_table': 'diseases',
                'unique_together': {('national', 'disease_name')},
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('person1', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.person')),
                ('relation', models.CharField(blank=True, null=True)),
                ('person2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='relationship_person2_set', to='users.person')),
            ],
            options={
                'db_table': 'relationship',
                'unique_together': {('person1', 'person2')},
            },
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('receiver', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.person')),
                ('reception_id', models.DateField()),
                ('blood_group', models.TextField()),
                ('quantity', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('blood', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.blood')),
            ],
            options={
                'db_table': 'reception',
                'unique_together': {('receiver', 'blood')},
            },
        ),
    ]
