from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from . import views

router = DefaultRouter()

router.register(r'categoria',views.CategoriaView,basename='categoria')
router.register(r'producto', views.ProductoView,basename='producto')

#urlpatterns = [
#    path('',views.IndexView.as_view()),
#    path('categoria_create',views.CategoriaView.as_view()),
#    path('productos',views.ProductoView.as_view()),
    # Ruta para crear nuevo producto
#    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),
#   path('admin/',include(router.urls)),
#   path('productoCrear', views.ProductoCreate.as_view()),
#   path('categorias', views.categoriaLista.as_view()),
#]
urlpatterns = [
   path("v1/", include(router.urls)),
   path("docs/", include_docs_urls(title="tienda_Api"))
]
