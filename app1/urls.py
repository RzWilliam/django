from django.urls import path
from . import views

app_name='app1'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_view, name='create_view'),
    path('show', views.list_view, name='list_view'),
    path('show/<id>', views.detail_view,  name='detail_view'),
    path('update/<id>', views.update_view, name='update_view'),
    path('delete/<id>', views.delete_view, name='delete_view' )
]