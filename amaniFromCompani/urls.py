from django.urls import path
from . import views
app_name = "amaniFromCompani"
urlpatterns = [
    path("",views.amaniHome_view,name="amani_home"),
    path("product-registration/",views.amaniProductRegistration_view,name="amani_productRegistration"),
    path("product-registration-edit/",views.amaniProductRegistrationEdit_view,name="amani_productRegistrationEdit"),
    path("product-registration-delete/",views.amaniProductRegistrationDelete_view,name="amani_productRegistrationDelete"), 
    path("delivered-products/",views.amaniDeliveredProducts,name="amani_delivered-products"),
    path("export-excel/",views.amaniExport_excel_view,name="amani_export_excel"), 
    path("export-pdf/",views.amaniExport_pdf_view,name="amani_export_pdf"),
    path("stop-page/",views.amaniStop_view,name="amani_stop"),
    path("check-password-edit/<int:id>/",views.amaniCheck_password_edit_view,name="amani_check_password_edit"),
    path("check-password-delete/<int:id>/",views.amaniCheck_password_delete_view,name="amani_check_password_delete"),  
      
]