from django.contrib import admin
from django.http import HttpResponse
import csv

from .models import Estudiante, Curso, Direccion, Profesor

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    actions = ["export_to_csv"]
    
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="estudiantes.csv"'
        writer = csv.writer(response)
        writer.writerow(["RUT", "Nombre", "Apellido", "Fecha de Nacimiento", "Dirección"])
        for estudiante in queryset:
            writer.writerow(
                [
                    estudiante.rut,
                    estudiante.nombre,
                    estudiante.apellido,
                    estudiante.fecha_nac,
                    estudiante.direccion,
                    
                ]
            )
        return response

    export_to_csv.short_description = "Exportar estudiantes seleccionados a CSV"


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    actions = ["export_to_csv"]
    readonly_fields = ('creacion_registro', 'modificacion_registro', 'creado_por')

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="cursos.csv"'
        writer = csv.writer(response)
        writer.writerow(["Código", "Nombre", "Versión", "Profesor", "Activo", "Creación de Registro", "Modificación de Registro", "Creado Por"])
        for curso in queryset:
            writer.writerow(
                [
                    curso.codigo,
                    curso.nombre,
                    curso.version,
                    curso.profesor,
                    curso.activo,
                    curso.creacion_registro,
                    curso.modificacion_registro,
                    curso.creado_por,
                ]
            )
        return response

    export_to_csv.short_description = "Exportar cursos seleccionados a CSV"


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    actions = ["export_to_csv"]
    readonly_fields = ('creacion_registro', 'modificacion_registro', 'creado_por')

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="profesores.csv"'
        writer = csv.writer(response)
        writer.writerow(["RUT", "Nombre", "Apellido", "Activo", "Creación de Registro", "Modificación de Registro", "Creado Por"])
        for profesor in queryset:
            writer.writerow(
                [
                    profesor.rut,
                    profesor.nombre,
                    profesor.apellido,
                    profesor.activo,
                    profesor.creacion_registro,
                    profesor.modificacion_registro,
                    profesor.creado_por,
                ]
            )
        return response

    export_to_csv.short_description = "Exportar profesores seleccionados a CSV"


@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    actions = ["export_to_csv"]
    
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="direcciones.csv"'
        writer = csv.writer(response)
        writer.writerow(["ID", "Calle", "Número", "Departamento", "Comuna", "Ciudad", "Región"])
        for direccion in queryset:
            writer.writerow(
                [
                    direccion.id,
                    direccion.calle,
                    direccion.numero,
                    direccion.dpto,
                    direccion.comuna,
                    direccion.ciudad,
                    direccion.region,
                ]
            )
        return response

    export_to_csv.short_description = "Exportar direcciones seleccionadas a CSV"
