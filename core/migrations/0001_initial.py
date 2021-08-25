# Generated by Django 3.2.6 on 2021-08-25 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemCategory', models.CharField(help_text='item category', max_length=100)),
                ('brand', models.CharField(help_text='brand of the item', max_length=100)),
                ('price', models.IntegerField(help_text='price for the item')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(help_text='username', max_length=100)),
                ('walletAmount', models.IntegerField(help_text='wallet amount')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text='quantity for the item')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.item')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text='quantity for the item')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.user')),
            ],
        ),
    ]
