from django.contrib import admin

# Register your models here.

from .models import Molecule, Activity, Target

admin.site.register(Molecule)
admin.site.register(Activity)
admin.site.register(Target)
