from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EquipoFutbol, Jugador, Campeonato, CampeonatoEquipos
from import_export.admin import ImportExportModelAdmin

admin.site.register(EquipoFutbol, ImportExportModelAdmin)
admin.site.register(Jugador, ImportExportModelAdmin)
admin.site.register(Campeonato, ImportExportModelAdmin)
admin.site.register(CampeonatoEquipos, ImportExportModelAdmin)
