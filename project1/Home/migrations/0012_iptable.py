# Generated by Django 4.2.3 on 2023-09-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_alter_rrfimage_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('ip1', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]