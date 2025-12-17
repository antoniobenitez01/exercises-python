from django.db import models
# Create your models here.
# Al aplicar esta herencia, Django va sa saber que Author es una tabla en la BD
class Author (models.Model):
    name=models.CharField (verbose_name='Nombre', # etiqueta dentro de la tabla
    max_length= 100,
    default=''
    )
    last_name=models.CharField(verbose_name='Apellido',
    max_length=150,
    default='')
    age=models.PositiveSmallIntegerField (verbose_name='Edad',
    )
    #Añadimos este código para que en el administrador al acceder a los
    # registros que contiene la tabla aparezca no Author object ID, sino que nos
    # de más información del registro que hay dentro.
    #Con el método __str__, sobreescribimos la información por defecto.Indicamos
    # ahí lo que queramos que nos retorne
    #Ojo, está dentro de la clase
    def __str__(self):
        return f'{self.name} {self.last_name}'
    
class Book (models.Model):
    
    title=models.CharField('Título del libro',max_length=255,unique=True)
    cod=models.CharField('Codigo',max_length=15,unique=True)
    author=models.OneToOneField(Author,on_delete=models.CASCADE)
    author=models.OneToOneField(Author,on_delete=models.SET_NULL,null=True)
    author=models.ForeignKey(Author,null=True,blank=True,on_delete=models.CASCADE)
    author=models.ManyToManyField(Author)
