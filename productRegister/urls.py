from django.urls import path,include
from . import views


app_name = "productRegister"

urlpatterns = [
    path("",views.home_view,name="home"),
    path("product-registration/",views.productRegistration_view,name="productRegistration"),
    path("product-registration-edit/<int:id>/",views.productRegistrationEdit_view,name="productRegistrationEdit"),
    path("product-registration-delete/<int:id>/",views.productRegistrationDelete_view,name="productRegistrationDelete"), 
    path("delivered-products/",views.deliveredProducts,name="delivered-products"), 
]