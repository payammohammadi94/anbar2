from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import productRegisterForm,SearchBoxForm
from .models import productRegistrationModel
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

@login_required(login_url='/accounts/login/')
def home_view(request):
    return render(request,'productRegister/index.html')



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
                return HttpResponse("just super user can save data")
        else:
            return HttpResponse("data is not valid")


    return render(request,"productRegister/product-register.html",{})



@login_required(login_url='/accounts/login/')
def deliveredProducts(request):
    if request.user.is_superuser:
        
        search_form_data = SearchBoxForm(request.GET)
        
        if search_form_data.is_valid():

            search_text_form = search_form_data.cleaned_data["search_text"]
            print(search_text_form)
            
            data = productRegistrationModel.objects.filter(Q(user__username__contains=search_text_form) | Q(first_last_name__contains=search_text_form))
        else:
            data = productRegistrationModel.objects.all().order_by('-create')
        
        context = {"datas":data}
        return render(request,"productRegister/delivered-products.html",context)