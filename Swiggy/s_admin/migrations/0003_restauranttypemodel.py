# Generated by Django 3.0.5 on 2020-04-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_admin', '0002_areamodel_citymodel_statemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantTypeModel',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=50)),
            ],
        ),
    ]
