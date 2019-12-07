
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('formulario/', views.formula, name='formula'),
    path('products/', views.products, name='products'),
    path('store/', views.store, name='store'),
    path('formularios/', views.ListaformularioVista.as_view(), name='formularios'),
    path('formularios/<int:pk>', views.ListaformularioVista.as_view(), name='formulario-detail'),

]

urlpatterns+= [
    path('formulario/create', views.FormularioCreate.as_view(), name='formulario_create'),
    path('formulario/int:pk/update', views.FormularioUpdate.as_view(), name='formulario_update'),
    path('formulario/int:pk/delete', views.FormularioDelete.as_view(), name='formulario_delete'),
]
