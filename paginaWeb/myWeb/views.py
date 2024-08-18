from django.shortcuts import render, redirect
from .models import Navbar, Servicio, Proyecto, Contacto
from .forms import ContactoForm

def index(request):
    Navbars = Navbar.objects.all()
    Servicios = Servicio.objects.filter(vigente=True)
    Proyectos = Proyecto.objects.all()

    # Crear pares de proyectos
    proyectos_pares = []
    for i in range(len(Proyectos) - 1):
        proyectos_pares.append((Proyectos[i], Proyectos[i + 1]))
    

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')  # Redirige a la página de agradecimiento si es válido
    else:
        form = ContactoForm()

    context = {
        "Navbars": Navbars,
        "Servicios": Servicios,
        "Proyectos": Proyectos,
        'form': form,
    }

    return render(request, 'myWeb/index.html', context)

def contacto(request):
    Navbars = Navbar.objects.all()

    context = {"Navbars" : Navbars}

    return render(request, 'myWeb/contacto.html', context)

