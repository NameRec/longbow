# Generated by Django 2.1 on 2018-08-13 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('longbow', '0003_auto_20180813_0232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testpassing',
            old_name='stat_count_answers',
            new_name='stat_count_questions',
        ),
        migrations.AlterUniqueTogether(
            name='testingpassinganswer',
            unique_together={('test_passing_question', 'answer')},
        ),
    ]