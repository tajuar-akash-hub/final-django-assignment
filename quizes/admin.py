from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.quiz_model)
admin.site.register(models.quiz_Question)
admin.site.register(models.quiz_history_of_user)
admin.site.register(models.Choice)
admin.site.register(models.Quiz_rating_model)
admin.site.register(models.quiz_answer)
