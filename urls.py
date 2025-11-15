from django.urls import path
from . import views

urlpatterns = [
    path('', views.autor_list, name='autor_list'),
    path('autor/novo/', views.autor_create, name='autor_create'),
    path('autor/<int:pk>/editar/', views.autor_update, name='autor_update'),
    path('autor/<int:pk>/apagar/', views.autor_delete, name='autor_delete'),
    path('autor/<int:pk>/', views.autor_detail, name='autor_detail'),
]
