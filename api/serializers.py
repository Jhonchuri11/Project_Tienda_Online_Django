from rest_framework import serializers

from tienda.models import Categoria,Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):

    # Cuando se tiene una relacion de tabla uno a muchos
    # En este caso, al momento de ser usado el API
    # Para mostrar la data o el campo relacionado como el nombre de la categoria
    # Se agregan estan instancias que permiten obtener la data
    categoriaid = CategoriaSerializer()
    categoriaid = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    categoria_nombre = serializers.ReadOnlyField(source='categoriaid.nombre')
    
    # ------------------------------------------
    class Meta:
        model = Producto
        fields = ['codigo', 'descripcion', 'precio', 'categoriaid', 'categoria_nombre']
        #fields = '__all__'

    #def create(self, validated_data):
     #   categoria_data = validated_data.pop('categoria')
      #  categoria_instance = Categoria.objects.create(**categoria_data)

       # producto_instance = Productos.objects.create(categoria=categoria_instance, **validated_data)
        #return producto_instance