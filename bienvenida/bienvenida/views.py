from django.http import HttpResponse

def inicio(request):
    nombre = "Maythem Torres"
    return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")