from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from estudiantes.models import Estudiante


# Create your views here.
#def bienvenida(request):
 #   return HttpResponse('Saludos')

def bienvenida(request):
    cantidad_estudiantes = Estudiante.objects.count()
    # personas = Persona.objects.all()
    estudiantes = Estudiante.objects.order_by('apellido', 'nombre')
    dict_datos = {'cantidad_estudiantes':cantidad_estudiantes, 'personas':estudiantes}
    pagina = loader.get_template('bienvenida.html')
    return HttpResponse(pagina.render(dict_datos,request))
