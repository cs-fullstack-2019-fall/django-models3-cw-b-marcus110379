from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.addBook),
    path('all/', views.allBook),

    path('', views.index, name='index'),
]


# path('printsome/',views.printOnly)