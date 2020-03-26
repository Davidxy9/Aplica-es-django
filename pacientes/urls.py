from django.urls import path
from pacientes.views import list, create, list1, create1, virus_update, virus_delete

urlpatterns = [
    path('list/', list, name="list"),
    path('create/', create, name="create"),
    path('list1/', list1, name="list1"),
    path('create1/', create1, name="create1"),
    path('update/<int:id>/', virus_update, name="virus_update"),
    path('delete/<int:id>/', virus_delete, name="virus_delete"),
]