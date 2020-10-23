from django.contrib import admin

# Register your models here.

from.models import carrera
from.models import Paralelo
from.models import Profesor

admin.site.register(carrera)
admin.site.register(Paralelo)
admin.site.register(Profesor)
