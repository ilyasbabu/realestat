# Generated by Django 4.0.4 on 2022-05-05 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vehichle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('locality', models.CharField(max_length=50)),
                ('fuel', models.CharField(max_length=50)),
                ('reg_year', models.IntegerField()),
                ('kilometers', models.IntegerField(blank=True, null=True)),
                ('gear_Type', models.CharField(blank=True, max_length=20, null=True)),
                ('postedOn', models.DateTimeField(auto_now_add=True)),
                ('ownership', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField()),
                ('contact_details', models.TextField()),
                ('main_image', models.ImageField(upload_to='images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.district')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('locality', models.CharField(max_length=50)),
                ('land_area', models.CharField(max_length=50)),
                ('electricity_available', models.BooleanField(default=False)),
                ('source_of_water', models.CharField(blank=True, max_length=50, null=True)),
                ('built_year', models.CharField(blank=True, max_length=50, null=True)),
                ('buildin_area', models.CharField(blank=True, max_length=50, null=True)),
                ('bedrooms', models.IntegerField(blank=True, null=True)),
                ('postedOn', models.DateTimeField(auto_now_add=True)),
                ('ownership', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField()),
                ('furniture_available', models.BooleanField(default=False)),
                ('contact_details', models.TextField()),
                ('main_image', models.ImageField(upload_to='images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_6', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_7', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_8', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_9', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.district')),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.propertytype')),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.purpose')),
            ],
        ),
    ]
