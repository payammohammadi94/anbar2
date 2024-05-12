from django.urls import path,include
from . import views


app_name = "productRegister"

urlpatterns = [
    path("",views.home_view,name="home"),
    path("product-registration/",views.productRegistration_view,name="productRegistration"),
    path("product-registration-edit/",views.productRegistrationEdit_view,name="productRegistrationEdit"),
    path("product-registration-delete/",views.productRegistrationDelete_view,name="productRegistrationDelete"), 
    path("delivered-products/",views.deliveredProducts,name="delivered-products"),
    path("export-excel/",views.export_excel_view,name="export_excel"), 
    path("export-pdf/",views.export_pdf_view,name="export_pdf"),
    path("stop-page/",views.stop_view,name="stop"),
    path("check-password-edit/<int:id>/",views.check_password_edit_view,name="check_password_edit"),
    path("check-password-delete/<int:id>/",views.check_password_delete_view,name="check_password_delete"),  
      
      
]