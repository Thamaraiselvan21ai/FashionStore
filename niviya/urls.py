from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
      path('login/',views.loginhtml, name='loginhtml'),
      path('',views.indexhtml, name='indexhtml'),

      path('home/<int:nu>',views.returnhome, name='returnhome'),
      path('products/<int:nu>',views.returnproducts, name='returnproducts'),
      path('categories/<int:nu>',views.returncategori, name='returncategori'),
      path('contact/<int:nu>',views.returncontact, name='returncontact'),
      # path('index/products/',views.productshtml, name='productshtml'),
      # path('products/categories/',views.categorieshtml, name='categorieshtml'),
      # path('products/contact/',views.contacthtml, name='categorieshtml'),
      # path('contact/',views.contacthtml, name='contacthtml'),
      # path('Niviya/',views.Niviyahtml, name='Niviyahtml'),
      path('login/',views.loginhtml, name='signhtml'),
      path('login/signin/',views.signin, name='signin'),
      path('login/sign/',views.signhtml, name='signhtml'),
      path('login/sign/back/',views.back, name='back'),
      path('login/sign/createuser/',views.createuser, name='createuser'),
      # path('products/categories/contact/login/',views.indexhtml1, name='indexhtml'),
]

