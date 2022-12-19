# Generated by Django 3.2.5 on 2022-12-18 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='shop_detail',
        ),
        migrations.AddField(
            model_name='shop',
            name='supplier',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
