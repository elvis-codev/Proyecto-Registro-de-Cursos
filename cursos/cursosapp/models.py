from django.db import models

# Create your models here.
class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    direccion = models.OneToOneField('Direccion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesor = models.ManyToManyField('Profesor', related_name='cursos')
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField()
    modificacion_registro = models.DateField()
    creado_por = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.dpto}, {self.comuna}, {self.ciudad}, {self.region}"

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"
        ordering = ["id"]

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField()
    modificacion_registro = models.DateField()
    creado_por = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["rut"]