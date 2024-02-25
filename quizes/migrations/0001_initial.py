# Generated by Django 5.0 on 2024-02-20 01:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catagories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_Answer', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='quiz_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('quiz_description', models.CharField(max_length=50)),
                ('time_limit', models.BooleanField(default=False)),
                ('creation_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=None)),
                ('quiz_banner', models.ImageField(blank=True, null=True, upload_to=None)),
                ('quiz_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catagories.category_model')),
            ],
        ),
        migrations.CreateModel(
            name='quiz_history_of_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('totalMarks', models.IntegerField(default=0)),
                ('completed_time', models.DateTimeField(auto_now_add=True)),
                ('certificate', models.FileField(blank=True, null=True, upload_to='certificates/')),
                ('selected_choices', models.ManyToManyField(blank=True, related_name='selected_choices', to='quizes.choice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.quiz_model')),
            ],
        ),
        migrations.CreateModel(
            name='quiz_Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizQuestion', models.CharField(max_length=255)),
                ('quizMark', models.IntegerField(default=1)),
                ('quiz', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quizes.quiz_model')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='quiz_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.quiz_question'),
        ),
        migrations.CreateModel(
            name='Quiz_rating_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_rating', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.quiz_model')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]