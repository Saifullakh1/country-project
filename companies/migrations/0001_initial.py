# Generated by Django 4.1.2 on 2023-07-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='company_logo')),
                ('address', models.CharField(max_length=150)),
                ('finance', models.IntegerField(default=0)),
                ('personals', models.ManyToManyField(related_name='company_personals', to='users.user')),
            ],
        ),
    ]
