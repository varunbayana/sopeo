# Generated by Django 4.1.7 on 2023-03-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sope', '0003_alter_employee_leave_count_alter_employee_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='DOB',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='DOJ',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Leave_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]