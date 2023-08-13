from django.urls import path
from  . import views


urlpatterns = [
    path('',views.index,name="home"),
    path('new',views.new,name="new products"),
    path('about',views.about,name="about products"),
    path('price',views.price,name="price "),
    path('quantity',views.quantity,name="quantity"),
    path('contact',views.contact,name="contact")

]

