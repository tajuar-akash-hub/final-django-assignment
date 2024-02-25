# Generated by Django 5.0 on 2024-02-23 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz_question',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions_tracker', to='quizes.quiz_model'),
        ),
        migrations.CreateModel(
            name='quiz_answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_answer', models.CharField(max_length=50)),
                ('quiz_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_tracker', to='quizes.quiz_question')),
            ],
        ),
    ]
