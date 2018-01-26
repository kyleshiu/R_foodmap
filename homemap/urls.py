from django.urls import path
from . import views

app_name='homemap'
urlpatterns=[
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path("select/",views.select,name='select'),
    path('foodcollection/',views.foodcollection,name='foodcollection'),
    path('about/',views.about,name='about'),
]