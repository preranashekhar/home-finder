# Generated by Django 3.1.2 on 2020-11-09 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20201106_2248'),
        ('home_listing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteSearches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('query_params', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('deleted_why', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('deleted_why', models.TextField(null=True)),
                ('home_listing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home_listing.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.user')),
            ],
        ),
    ]
