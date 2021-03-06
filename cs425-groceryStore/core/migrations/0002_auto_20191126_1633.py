# Generated by Django 2.2.7 on 2019-11-26 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='alcohol_content',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Alcohol', 'Alcohol'), ('Snack', 'Snack'), ('Dairy', 'Dairy'), ('Cereal', 'Cereal'), ('Other', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='nutrition',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
