from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
    
class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    categoriaid = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
    


    


