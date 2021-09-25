# Generated by Django 3.2.7 on 2021-09-25 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fivecode', '0002_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fivecode.empresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(),
        ),
    ]