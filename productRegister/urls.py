from django.urls import path,include
from . import views


app_name = "productRegister"

urlpatterns = [
    path("",views.home_view,name="home"),
    path("product-registration/",views.productRegistration_view,name="productRegistration"),
    path("delivered-products/",views.deliveredProducts,name="delivered-products"), 
]