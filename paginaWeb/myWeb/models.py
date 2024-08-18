from django.db import models

# Create your models here.
class Navbar(models.Model):
    id_navbar   = models.AutoField(db_column = 'idNavbar',primary_key=True)
    navbar      = models.CharField(max_length=30, blank = True,  null = True)
    url         = models.CharField(max_length=100,null=True ,blank = True,)

    """def __str__(self):
        return str(self.navbar)"""

class Servicio(models.Model):
    id_navbar         = models.AutoField(db_column = 'idServicio',primary_key=True)
    nombre_servicio   = models.CharField(max_length=50, blank = True,  null = True)
    img_servicio      = models.CharField(max_length=100,null=True ,blank = True,)
    descripcion       = models.TextField(null=True ,blank = True)
    vigente           = models.BooleanField(default=True)

class Proyecto(models.Model):
    id_proyecto       = models.AutoField(db_column = 'idProyecto',primary_key=True)
    nombre_proyecto   = models.CharField(max_length=50, blank = True,  null = True)
    img_proyecto      = models.CharField(max_length=100,null=True ,blank = True,)
    descripcion       = models.TextField(null=True ,blank = True)
    vigente           = models.BooleanField(default=True)

class Contacto(models.Model):
    id_contacto = models.AutoField(db_column='idContacto', primary_key=True)
    nombre_contacto = models.CharField(max_length=50, blank=True, null=True)
    apellidos_contacto = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    mensaje = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre_contacto} {self.apellidos_contacto}'