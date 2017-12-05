from django.http import HttpResponse
from . import tasks

def index(request):
    return HttpResponse("""
Rutas principales

<ul>
    <li><a href="/crearTarea">Crear tarea</a></li>
    <li><a href="/demo">Demo</a></li>
</ul>


""")


def demo(request):
    return HttpResponse("Demo!")

def crearTarea(request):
    tarea = tasks.add.delay(2, 3)
    return HttpResponse("Creando tarea: " + str(tarea))
