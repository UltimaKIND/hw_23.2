# Generated by Django 5.1.1 on 2024-09-17 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_options_alter_release_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ('version_name',), 'permissions': [('can_edit_is_active', 'can cancel publication'), ('can_edit_version', 'can edit version')], 'verbose_name': 'версия', 'verbose_name_plural': 'версии'},
        ),
        migrations.AlterField(
            model_name='release',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
