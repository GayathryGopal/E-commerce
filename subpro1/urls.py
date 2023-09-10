from django.urls import path
from subpro1 import views
urlpatterns=[
    path('',views.home),
    path('hm',views.home),
    path("rg",views.regist),
    
    path('log',views.login),
    path('ahome',views.adminhome),
    
    path('vstaff',views.vwstaff),
    path('adstaff',views.addstaff),
    
    path('vwprdct',views.viewproduct),
    path('adprdct',views.addproduct),
    path('shome',views.staffhome),
   
    path('vmore',views.more),
    path('uhome',views.userhome),
    path('top',views.tops),
    path('tmore',views.mores),
    path('drs',views.dress),
    path('chpl',views.chappal),
    path('skrt',views.skirt),
    path('vwbuk',views.viewbuking),
    path('assign',views.assign),
    path('vwassign',views.viewassign),
    path('vwmywrk',views.viewmywork),
    path('dhome',views.deliveryhome),
    path('delivery',views.delivery),
    path('vwcmpltd',views.completedwork),
    path('myoder',views.myoder),
    path('deliverddtls',views.deliverddetails),
   
    
    
   
    
]