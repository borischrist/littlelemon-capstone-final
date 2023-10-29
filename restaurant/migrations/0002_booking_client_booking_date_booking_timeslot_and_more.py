# Generated by Django 4.2.5 on 2023-10-15 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='timeslot',
            field=models.SmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.category'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='inventory',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='photo',
            field=models.ImageField(blank=True, upload_to='uploads/menuitem-img/'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('date', 'timeslot')},
        ),
    ]