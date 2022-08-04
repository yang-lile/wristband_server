# Generated by Django 4.0.5 on 2022-07-05 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceinfo',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='deviceinfo',
            name='longitude',
        ),
        migrations.CreateModel(
            name='OxStart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_time', models.IntegerField(default=0)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='devices.device')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_time', models.IntegerField(default=0)),
                ('latitude', models.IntegerField(default=0)),
                ('longitude', models.IntegerField(default=0)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='devices.device')),
            ],
        ),
        migrations.CreateModel(
            name='Heartrate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_time', models.IntegerField(default=0)),
                ('heart', models.SmallIntegerField(default=0)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='devices.device')),
            ],
        ),
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_time', models.IntegerField(default=0)),
                ('systolic_blood', models.PositiveSmallIntegerField(default=0)),
                ('diastolic_blood', models.PositiveSmallIntegerField(default=0)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='devices.device')),
            ],
        ),
    ]
