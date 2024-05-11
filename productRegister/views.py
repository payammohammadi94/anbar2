from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import productRegisterForm,SearchBoxForm,productRegisterEditForm
from .models import productRegistrationModel
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
import xlwt
from datetime import datetime, timezone
from jalali_date import datetime2jalali
# Create your views here.




@login_required(login_url='/accounts/login/')
def home_view(request):
    return render(request,'productRegister/index.html')


#این برای ثبت محصولات است
@login_required(login_url='/accounts/login/')
def productRegistration_view(request):
    
    if request.method=="POST":
        product_data = productRegisterForm(request.POST)
        if product_data.is_valid():
            data_clean = product_data.cleaned_data
            
            


            user = data_clean["user"]
            first_last_name = data_clean["first_last_name"]
            prudoct_name = data_clean["prudoct_name"]
            prudoct_code = data_clean["prudoct_code"]
            
            username = User.objects.get(username=user)
            
            if request.user.is_superuser:
                if username:
                    productRegistrationModel.objects.create(user=username,first_last_name=first_last_name,prudoct_name=prudoct_name,prudoct_code=prudoct_code)
                    return redirect("productRegister:delivered-products")
                else:
                    return HttpResponse("this user is not found")
            else:
                return redirect("productRegister:stop")
        else:
            return HttpResponse("data is not valid")


    return render(request,"productRegister/product-register.html",{})



@login_required(login_url='/accounts/login/')

def productRegistrationEdit_view(request,id):
    if request.user.is_superuser:
        product_edit = productRegistrationModel.objects.get(pk=id)
        first_last_name = product_edit.first_last_name
        product_name = product_edit.prudoct_name
        product_code = product_edit.prudoct_code
        
    
        if request.method == "POST":
            product_form_edit = productRegisterEditForm(request.POST,instance=product_edit)
            if product_form_edit.is_valid():
                product_form_edit.save()
                return redirect("productRegister:delivered-products")
            else:
                return HttpResponse("form is not valid")
        else:
            product_form_edit = productRegisterEditForm(instance=product_edit)
        context = {"product_form_edit":product_form_edit,"first_last_name":first_last_name,"product_name":product_name,"product_code":product_code}
        return render(request,"productRegister/product-edit.html",context)
    else:
        return redirect("productRegister:stop")
        
    

def productRegistrationDelete_view(request,id):
    if request.user.is_superuser:
        product_delete = productRegistrationModel.objects.get(pk=id)
        product_delete.delete()      
        return redirect("productRegister:delivered-products")
    else:
        return redirect("productRegister:stop")
        




#برای نمایش محصولات است
@login_required(login_url='/accounts/login/')
def deliveredProducts(request):
    if request.user.is_superuser:
        
        search_form_data = SearchBoxForm(request.GET)
        
        if search_form_data.is_valid():

            search_text_form = search_form_data.cleaned_data["search_text"]
            
            
            data = productRegistrationModel.objects.filter(Q(user__username__contains=search_text_form) | Q(first_last_name__contains=search_text_form) | Q(prudoct_name__contains=search_text_form) | Q(prudoct_code__contains=search_text_form))
        else:
            data = productRegistrationModel.objects.filter(status=False).order_by('-create')
        
        context = {"datas":data}
        return render(request,"productRegister/delivered-products.html",context)
    else:
        return redirect("productRegister:stop")
    

# برای خروجی گرفتن اکسل
@login_required(login_url='/accounts/login/')   
def export_excel_view(request):
    if request.user.is_superuser:
        response = HttpResponse(content_type = "application/ms-excel")
        response["content-Disposition"] ='attachment;filename=delivered-products-'+str(datetime2jalali(datetime.now())).split(".")[0]+'.xls'
        
        workBook = xlwt.Workbook(encoding="utf-8")
        workSheet = workBook.add_sheet("delivered-products")
        
        columns = ["Username", "Full name", "Prudoct Name", "Prudoct Code", "Date-Time",]
        rowNumber = 0
        
        for col in range(len(columns)):
            workSheet.write(rowNumber,col,columns[col])
        
        data_for_excel = productRegistrationModel.objects.filter(status=False).order_by('-create').values_list(
            "user",
            "first_last_name",
            "prudoct_name",
            "prudoct_code",
            "create")
        
        for data in data_for_excel:
            rowNumber += 1

            for col in range(len(data)):
                if col==0:
                    workSheet.write(rowNumber,col,User.objects.get(pk=data[col]).username)
                
                
                elif col ==4:
                    workSheet.write(rowNumber,col,str(datetime2jalali(data[col])).split(".")[0])
                else:
                    workSheet.write(rowNumber,col,data[col])
        workBook.save(response)
        return response
    else:
        return redirect("productRegister:stop") 
    


def export_pdf_view(request):
    pass




def stop_view(request):
    return render(request,"productRegister/super-user-control.html")