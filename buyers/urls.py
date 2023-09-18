from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('byhome',BuyerHome.as_view(),name="byhome"),
    path('prod/<int:pid>',SpecView.as_view(),name="prod"),
    path('Aucart/<int:id>',bidcart,name="Amtcart"),
    path('bidpage',BidPriceView.as_view(),name="bidpage"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)