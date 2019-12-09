# Generated by Django 2.2.4 on 2019-12-09 15:48

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20191203_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-likecnt']},
        ),
        migrations.AddField(
            model_name='photo',
            name='likecnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='photo',
            name='hashtag',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]