from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
import xlwt
from datetime import datetime, timezone
from jalali_date import datetime2jalali
from django.contrib.auth.hashers import check_password

from .models import amaniProductRegistrationModel
from .forms import amaniProductRegisterForm, amaniSearchBoxForm, amaniProductRegisterEditForm, amaniCheckPasswordForm

# Create your views here.



def amaniHome_view(request):
    pass


def amaniProductRegistration_view(request):
    pass


def amaniProductRegistrationEdit_view(request):
    pass


def amaniProductRegistrationDelete_view(request):
    pass


def amaniDeliveredProducts(request):
    pass


def amaniExport_excel_view(request):
    pass


def amaniExport_pdf_view(request):
    pass


def amaniStop_view(request):
    pass


def amaniCheck_password_edit_view(request,id):
    pass


def amaniCheck_password_delete_view(request,id):
    pass


      