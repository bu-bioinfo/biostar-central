# Generated by Django 2.2.7 on 2020-01-23 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_watched_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.IntegerField(choices=[(0, 'Reader'), (1, 'Moderator'), (2, 'Admin'), (3, 'Blog User')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Active'), (4, 'Spammer'), (2, 'Suspended'), (3, 'Banned')], db_index=True, default=0),
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.IntegerField(choices=[(0, 'User preformed a moderation action.'), (1, 'User created an object.'), (2, 'User edited an object.'), (3, 'User logged in to the site.'), (4, 'User logged out of the site.'), (5, 'User browsing the site.')], default=5)),
                ('log_text', models.TextField(default='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('target', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='target', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
