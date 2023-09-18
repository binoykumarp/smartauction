from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView
from account.models import Product,Aucart,Room
from django.contrib import messages

from datetime import datetime
from django.utils import timezone

# Create your views here.

class BuyerHome(View):
    def get(self,request):
        products=Product.objects.all()
        current_date = timezone.now().date()
        bid_prod=Product.objects.filter(Au_Date=current_date).first()
        aucart=Aucart.objects.filter(product=bid_prod)
        aucart_ob=None
        money=0
        for i in aucart:
            if i.money > money:
                money=i.money
                aucart_ob=i
        print(aucart_ob)
        return render(request,"byerhome.html",{"pro":products,"b_pro":aucart_ob})

class BidPriceView(View):
    def get(self,request,*args,**kwargs):
        current_date = timezone.now().date()
        bid_prod=Product.objects.filter(Au_Date=current_date).first()
        aucart=Aucart.objects.filter(product=bid_prod)
        aucart_ob=None
        money=0
        for i in aucart:
            if i.money > money:
                money=i.money
                aucart_ob=i
        print(aucart_ob)
        # room=Room.objects.get(user=self.request.user)
        return render(request,"chatbox.html",{"b_pro":aucart_ob})

class SpecView(DetailView):
    template_name="specificview.html"
    queryset=Product.objects.all()
    pk_url_kwarg="pid"
    context_object_name="data"


def bidcart(request,*args,**kwargs):
    pid=kwargs.get("id")
    pro=Product.objects.get(id=pid)
    user=request.user
    qty=request.POST.get("amt")
    Aucart.objects.create(product=pro,user=user,money=qty)
    messages.success(request,"Amount Updated...")
    return redirect('bidpage')

class BidpageView(TemplateView):
    template_name="chatbox.html"