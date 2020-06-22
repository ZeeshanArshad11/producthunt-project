# Generated by Django 2.1.5 on 2020-06-10 12:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20200610_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voting',
            old_name='product',
            new_name='products',
        ),
        migrations.AlterUniqueTogether(
            name='voting',
            unique_together={('user', 'products')},
        ),
        migrations.AlterIndexTogether(
            name='voting',
            index_together={('user', 'products')},
        ),
    ]