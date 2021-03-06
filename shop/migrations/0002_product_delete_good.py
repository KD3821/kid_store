# Generated by Django 4.0.4 on 2022-05-30 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer', models.CharField(max_length=200)),
                ('price', models.IntegerField(max_length=5)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория')),
            ],
        ),
        migrations.DeleteModel(
            name='Good',
        ),
    ]
