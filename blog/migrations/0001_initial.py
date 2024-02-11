# Generated by Django 4.2.7 on 2023-12-10 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('preview', models.ImageField(blank=True, upload_to='blog_imgs')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]