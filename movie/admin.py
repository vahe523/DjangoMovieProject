from django.contrib import admin
from movie import models

admin.site.register(models.Movie)
admin.site.register(models.Genre)