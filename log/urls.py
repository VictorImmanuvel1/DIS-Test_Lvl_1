from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='adminHome'),
    path('register/',views.register,name="staffReg"),
    path('view/<str:pk_test>/',views.info,name='viewpage'),
    path('update/<str:pk_test>/',views.update,name='updatepage'),
    path('updatemark/<str:pk_test>/',views.updatemark,name='updatemark'),
    path('delete/<str:pk>/',views.delete,name='deleteuser'),
    path('markupdate/',views.markupdate,name='markupdate')
]