# Generated by Django 2.2.5 on 2020-07-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QandS', '0003_q_shotlist_awnsr_qna'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='q_shotlist',
            name='awnsr_qna',
        ),
        migrations.AddField(
            model_name='postmodel_q',
            name='awnsr_qna',
            field=models.TextField(blank=True),
        ),
    ]
