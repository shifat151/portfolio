from django.contrib import admin
from .models import Language,Framework,Project,Academic,Profile

# Register your models here.
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Project)
admin.site.register(Academic)
admin.site.register(Profile)
