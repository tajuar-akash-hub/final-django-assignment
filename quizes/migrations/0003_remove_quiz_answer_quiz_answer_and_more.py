# Generated by Django 5.0 on 2024-02-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0002_alter_quiz_question_quiz_quiz_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz_answer',
            name='quiz_answer',
        ),
        migrations.AddField(
            model_name='quiz_answer',
            name='correct_quiz_answer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='quiz_answer',
            name='possible_quiz_answer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
