# Generated by Django 4.2.2 on 2023-07-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_rename_contact_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=122)),
                ('LastName', models.CharField(max_length=122)),
                ('Username', models.CharField(max_length=122)),
                ('Email', models.CharField(max_length=122)),
                ('reason', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='contacts',
        ),
    ]
