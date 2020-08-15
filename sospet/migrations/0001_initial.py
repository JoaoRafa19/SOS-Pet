# Generated by Django 3.0.8 on 2020-08-06 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('telefone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='')),
                ('ativo', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Pet',
            },
        ),
    ]