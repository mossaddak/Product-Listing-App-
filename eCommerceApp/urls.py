from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.AllProducts, name='AllProducts'),
    path('ProductDetails/<int:pk>/', views.ProductDetails, name="ProductDetails"),
    path('MyProducts/', views.MyProducts, name="MyProducts"),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('UpdateProduct/<int:pk>/', views.UpdateProduct, name="UpdateProduct"),
    path('DeleteProduct/<int:pk>/', views.DeleteProduct, name="DeleteProduct"),
    path('UserProductsForAdmin/', views.UserProductsForAdmin, name="UserProductsForAdmin"),
    path('AllUsers/', views.AllUsers, name="AllUsers"),
    path('UserProfile/<int:pk>/', views.UserProfile, name="UserProfile"),
    path('ProfilePictureChngeForAdmin/<int:pk>/', views.ProfilePictureChngeForAdmin, name="ProfilePictureChngeForAdmin"),
    path('SpecificUsersProductForAdmin/<int:pk>/', views.SpecificUsersProductForAdmin, name="SpecificUsersProductForAdmin")
]
