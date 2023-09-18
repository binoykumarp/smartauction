from django.shortcuts import render,redirect
from django.views.generic import View,ListView
from .forms import RegForm,LogForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import FormView,CreateView
from account.models import Product,Room
from django.urls import reverse_lazy


# Create your views here.

class LogView(FormView):
    # def get(self,request):
    #     f=LogForm()
    #     return render(request,'login.html',{"f":f})
    template_name="login.html"
    form_class=LogForm
    def post(self,request):
        fdata=LogForm(data=request.POST)
        if fdata.is_valid():
            ur=fdata.cleaned_data.get('username')
            ps=fdata.cleaned_data.get('password')
            user=authenticate(request,username=ur,password=ps)
            if user:
                login(request,user)
                
                return redirect('byhome')
            else:
                messages.error(request,"login failed! Invalid Username or Password")
                return redirect('log')
        return render(request,"login.html",{"f":fdata})
    
from django.utils.text import slugify
class RegView(View):
    def get(self,request):
        f=RegForm()
        return render(request,'reg.html',{"form":f})
    # form_class=RegForm
    # template_name="reg.html"
    # success_url=reverse_lazy('log')

    # def form_valid(self,form):
    #     messages.success(self.request,"Registration Successfull..!!")
    #     return super().form_valid(form)
    def post(self,request):
        fdata=RegForm(data=request.POST)
        if fdata.is_valid():
            instances=fdata.save()
            room_name = f"{instances.username} - {instances.id}"
            room_slug = slugify(room_name)
            Room.objects.create(user=instances,name=room_name,slug=room_slug)
            return redirect('log')
        return render(request,"reg.html",{"form":fdata})
    

class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
    

# class MainHome(ListView):
#     template_name="frontmain.html"
#     queryset=Product.objects.all()
#     context_object_name="pro"

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("home")