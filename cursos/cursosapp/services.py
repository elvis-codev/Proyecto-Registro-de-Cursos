from cursosapp.models import Estudiante, Profesor, Curso, Direccion

def crear_estudiante(rut, nombre, apellido, fecha_nac, direccion):
    estudiante = Estudiante(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, direccion=direccion)
    estudiante.save()
    return estudiante

def obtener_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

def crear_curso(codigo, nombre, version, activo, creacion_registro, modificacion_registro, creado_por):
    curso = Curso(codigo=codigo, nombre=nombre, version=version, activo=activo, creacion_registro=creacion_registro, modificacion_registro=modificacion_registro, creado_por=creado_por)
    curso.save()
    return curso

def obtener_curso(codigo):
    return Curso.objects.get(codigo=codigo)

def crear_direccion(calle, numero, comuna, ciudad, region):
    direccion = Direccion(calle=calle, numero=numero, comuna=comuna, ciudad=ciudad, region=region)
    direccion.save()
    return direccion

def obtener_direccion(id):
    return Direccion.objects.get(id=id)

def crear_profesor(rut, nombre, apellido, activo, creacion_registro, modificacion_registro, creado_por):
    profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creacion_registro=creacion_registro, modificacion_registro=modificacion_registro, creado_por=creado_por)
    profesor.save()
    return profesor

def obtener_profesor(rut):
    return Profesor.objects.get(rut=rut)

def agrega_profesor_a_curso(profesor, curso):
    curso.profesores.add(profesor)
    curso.save()

def agrega_cursos_a_estudiante(estudiante, cursos):
    for curso in cursos:
        estudiante.cursos.add(curso)
    estudiante.save()

def imprime_estudiante_cursos(estudiante):
    cursos = estudiante.cursos.all()
    for curso in cursos:
        print(curso.nombre)
