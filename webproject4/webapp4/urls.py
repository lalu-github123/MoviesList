from .import views
from django.urls import path
app_name = 'webapp4'

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add_movies,name='add_movies'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('show/<int:id>',views.show,name='show'),
]
