
from django.shortcuts import render
from django.http import HttpResponseRedirect
from subpro1 import dbconnection
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
    return render(request,"home.html",{}) 
def regist(request):
     if request.method=="POST":
        n=request.POST['n']
        a=request.POST['a']
        ad=request.POST['ad']
        ph=request.POST['ph']
        em=request.POST['em']
        pas=request.POST['ps']
        g=request.POST['gen']
        q=request.POST.getlist('qualification')
        sql='insert into user(Name,Age,Address,Gender,Qualification,Emailid,Password,Phno) values("'+n+'","'+a+'","'+ad+'","'+g+'","'+str(q)+'","'+em+'","'+pas+'","'+ph+'")'
        dbconnection.addrow(sql)
        sql="insert into logdata(Userid,Password,Utype) values('"+em+"','"+pas+"','User')"
        dbconnection.addrow(sql)
        
        return HttpResponseRedirect('rg')

     return render(request,"regist.html",{}) 

def login(request):
    if request.method=="POST":
        u=request.POST['us']
        ps=request.POST['p']
        sql="select * from logdata where Userid='"+u+"' and Password='"+ps+"'"
        data=dbconnection.selone(sql)  
        if data:
            request.session['us']=u
            if data[3]=="admin":
                return HttpResponseRedirect('ahome')
            elif data[3]=="Office staff":
                return HttpResponseRedirect('shome')
            elif data[3]=="User":
                return HttpResponseRedirect('uhome')
            elif data[3]=="Delivery boy":
                return HttpResponseRedirect('dhome')
            
                

    return render (request,"login.html",{})

def adminhome(request):
    
    return render(request,'admin/adminhome.html',{})


def vwstaff(request):
    sql="select * from staff"
    data=dbconnection.selall(sql)
    return render(request,'admin/viewstaff.html',{'b':data})

def addstaff(request):
    if request.method=="POST":
        n=request.POST['n']
        a=request.POST['a']
        ad=request.POST['ad']
        ads=request.POST['stype']
        ph=request.POST['ph']
        em=request.POST['em']
        pas=request.POST['ps']
        g=request.POST['gen']
        q=request.POST.getlist('qualification')
        sql='insert into staff(Name,Age,Address,Gender,Qualification,Emailid,Password,Stafftype,Phno) values("'+n+'","'+a+'","'+ad+'","'+g+'","'+str(q)+'","'+em+'","'+pas+'","'+str(ads)+'","'+ph+'")'

        dbconnection.addrow(sql)
        sql="insert into logdata(Userid,Password,Utype) values('"+em+"','"+pas+"','"+ads+"')"
        dbconnection.addrow(sql)
        
        
        return HttpResponseRedirect('adstaff')
    return render(request,'admin/addstaff.html',{})


def staffhome(request):
    
    return render(request,'staff/staffhome.html',{})






def addproduct(request):
    if request.method=="POST":
        id=request.POST['id']
        n=request.POST['n']
        f=request.POST['fb']
        pattern=request.POST['p']
        size=request.POST['s']
        country=request.POST['co']
        img=request.FILES['im']
        img1=request.FILES['im1']
        img2=request.FILES['im2']
        img3=request.FILES['im3']
        fs=FileSystemStorage()

        fs.save('subpro1/static/image/'+img.name,img)
        fs.save('subpro1/static/image/'+img1.name,img1)
        fs.save('subpro1/static/image/'+img2.name,img2)
        fs.save('subpro1/static/image/'+img3.name,img3)
        price=request.POST['pc']
        sql='insert into allproduct(Id1,Name,Fabric,Pattern,Sizes,Countryoforgin,Image,Price,Image1,Image2,Image3) values("'+id+'","'+n+'","'+f+'","'+pattern+'","'+size+'","'+country+'","'+img.name+'","'+price+'","'+img1.name+'","'+img2.name+'","'+img3.name+'")'
        dbconnection.addrow(sql)
        if id.startswith ("T"):
            sql='insert into top(Id1,Name,Fabric,Pattern,Sizes,Countryoforgin,Image,Price,Image1,Image2,Image3) values("'+id+'","'+n+'","'+f+'","'+pattern+'","'+size+'","'+country+'","'+img.name+'","'+price+'","'+img1.name+'","'+img2.name+'","'+img3.name+'")'
            dbconnection.addrow(sql)
           
            
        elif id . startswith("D"):
             sql='insert into dresses(Id1,Name,Fabric,Pattern,Sizes,Countryoforgin,Image,Price,Image1,Image2,Image3) values("'+id+'","'+n+'","'+f+'","'+pattern+'","'+size+'","'+country+'","'+img.name+'","'+price+'","'+img1.name+'","'+img2.name+'","'+img3.name+'")'
             dbconnection.addrow(sql)
             
        elif id . startswith("S"):
             sql='insert into skirts(Id1,Name,Fabric,Pattern,Sizes,Countryoforgin,Image,Price,Image1,Image2,Image3) values("'+id+'","'+n+'","'+f+'","'+pattern+'","'+size+'","'+country+'","'+img.name+'","'+price+'","'+img1.name+'","'+img2.name+'","'+img3.name+'")'
             dbconnection.addrow(sql)

             
        elif id . startswith("C"):
             sql='insert into chappal(Id1,Name,Fabric,Pattern,Sizes,Countryoforgin,Image,Price,Image1,Image2,Image3) values("'+id+'","'+n+'","'+f+'","'+pattern+'","'+size+'","'+country+'","'+img.name+'","'+price+'","'+img1.name+'","'+img2.name+'","'+img3.name+'")'
             dbconnection.addrow(sql)


       
        return HttpResponseRedirect('adprdct')    


    return render(request,'staff/addproduct.html',{})

def viewproduct(request):
    sql="select * from allproduct"
    data1=dbconnection.selall(sql)
    if request.POST.get('Top'):
        sql="select * from top"
        data2=dbconnection.selall(sql)
        return render(request,'staff/top.html',{'e':data2})
    elif request.POST.get('Dress'):
        sql="select * from dresses"
        data2=dbconnection.selall(sql)
        return render(request,'staff/top.html',{'e':data2})
    elif request.POST.get('Skirt'):
        sql="select * from skirts"
        data2=dbconnection.selall(sql)
        return render(request,'staff/top.html',{'e':data2})
    elif request.POST.get('Chappal'):
        sql="select * from chappal"
        data2=dbconnection.selall(sql)
        return render(request,'staff/top.html',{'e':data2})
           

    return render(request,'staff/viewproduct.html',{'d':data1})

# def top(request):
#     sql="select * from top"
#     data2=dbconnection.selall(sql)
#     return render(request,'staff/top.html',{'e':data2})

def more(request):
    data=request.GET['mid']
    if request.POST.get('delete'):
        sql="delete from top where Id1='"+data+"'"
        dbconnection.delrow(sql)
        sql="delete from dresses where Id1='"+data+"'"
        dbconnection.delrow(sql)
        sql="delete from chappal where Id1='"+data+"'"
        dbconnection.delrow(sql)
        sql="delete from skirts where Id1='"+data+"'"
        dbconnection.delrow(sql)
        sql="delete from allproduct where Id1='"+data+"'"
        dbconnection.delrow(sql)
    if request.POST.get('sub'):        
        n=request.POST['n']                     
        f=request.POST['fb']
        pattern=request.POST['p']
        size=request.POST['s']
        country=request.POST['co']        
        price=request.POST['pc']        
        sql='update allproduct set Name="'+n+'",Fabric="'+f+'",Pattern="'+pattern+'",Sizes="'+size+'",Countryoforgin="'+country+'",Price="'+price+'" where Id1="'+data+'" '
        dbconnection.uprow(sql)
        if data.startswith('T'):
            sql='update top set Name="'+n+'",Fabric="'+f+'",Pattern="'+pattern+'",Sizes="'+size+'",Countryoforgin="'+country+'",Price="'+price+'" where Id1="'+data+'" '
            dbconnection.uprow(sql)
        elif data.startswith('D'):
            sql='update dresses set Name="'+n+'",Fabric="'+f+'",Pattern="'+pattern+'",Sizes="'+size+'",Countryoforgin="'+country+'",Price="'+price+'" where Id1="'+data+'" '
            dbconnection.uprow(sql) 
        elif data.startswith('S'):
            sql='update skirts set Name="'+n+'",Fabric="'+f+'",Pattern="'+pattern+'",Sizes="'+size+'",Countryoforgin="'+country+'",Price="'+price+'" where Id1="'+data+'" '
            dbconnection.uprow(sql)
        elif data.startswith('C'):
            sql='update chappal set Name="'+n+'",Fabric="'+f+'",Pattern="'+pattern+'",Sizes="'+size+'",Countryoforgin="'+country+'",Price="'+price+'" where Id1="'+data+'" '
            dbconnection.uprow(sql)
            

    if data.startswith('T'):        
        sql="select * from top where Id1='"+data+"' "
        data1=dbconnection.selone(sql)
        return render(request,'staff/more.html',{'data':data1})
    elif data.startswith('D'):        
        sql="select * from dresses where Id1='"+data+"' "
        data1=dbconnection.selone(sql)
        return render(request,'staff/more.html',{'data':data1})
    elif data.startswith('C'):        
        sql="select * from chappal where Id1='"+data+"' "
        data1=dbconnection.selone(sql)
        return render(request,'staff/more.html',{'data':data1})
    elif data.startswith('S'):        
        sql="select * from skirts where Id1='"+data+"' "
        data1=dbconnection.selone(sql)
        return render(request,'staff/more.html',{'data':data1})

def userhome(request):
    return render(request,'user/userhome.html',{})

def tops(request):
    sql="select * from top"
    data=dbconnection.selall(sql)
    return render(request,'user/top.html',{'a':data})
def dress(request):
    sql="select * from dresses"
    data=dbconnection.selall(sql)
    return render(request,'user/dress.html',{'b':data})
def chappal(request):
    sql="select * from chappal"
    data=dbconnection.selall(sql)
    return render(request,'user/chappal.html',{'c':data})
def skirt(request):
    sql="select * from skirts"
    data=dbconnection.selall(sql)
    return render(request,'user/skirt.html',{'d':data})   
def mores(request):
    data=request.GET['tid']
    if data.startswith('T'): 
        sql="select * from top where Id1='"+data+"' "
        data1=dbconnection.selone(sql)
    elif data.startswith('D'): 
        sql="select * from dresses where Id1='"+data+"' "
        data1=dbconnection.selone(sql)
    elif data.startswith('C'): 
        sql="select * from chappal where Id1='"+data+"' "
        data1=dbconnection.selone(sql)
    elif data.startswith('S'): 
        sql="select * from skirts where Id1='"+data+"' "
        data1=dbconnection.selone(sql)
    if request.method=="POST":
        pid=request.POST['id']
        n=request.POST['n']
        add=request.POST['ad']
        ph=request.POST['ph']        
        price=request.POST['pc']
        em=request.session['us']
        sql='insert into buynow(Userid,ProductId,Price,Name,Address,Phno,Status,Deliveryboy) values("'+em+'","'+pid+'","'+price+'","'+n+'","'+add+'","'+ph+'","0","not assigned")'
        dbconnection.addrow(sql)
        return HttpResponseRedirect('tmore?tid='+data)
    
    return render(request,'user/mores.html',{'c':data1})
    
def viewbuking(request):
    sql="select * from buynow where status=0"
    data=dbconnection.selall(sql)
    return render(request,'staff/viewbooking.html',{'ac':data})

def assign(request):      
    sql="select * from staff where Stafftype= 'Delivery boy'"
    data1=dbconnection.selall(sql)
    if request.method=="POST":
        data=request.GET['proid']      
        staff=request.POST['stype']
        sql="update buynow set status='1',Deliveryboy='"+staff+"' where id='"+data+"'"
        dbconnection.uprow(sql)
        return HttpResponseRedirect('assign?proid='+data)
    return render(request,'staff/assign.html',{'h':data1})
def viewassign(request):
    sql="select * from buynow where status=1"
    data=dbconnection.selall(sql)
    return render(request,'staff/viewassign.html',{'x':data})

def deliveryhome(request):
    return render(request,'deliveryboy/deliveryhome.html',{})
def viewmywork(request):
    em=request.session['us']
    sql="select * from buynow where status=1 and Deliveryboy='"+em+"' "
    data=dbconnection.selall(sql)
    return render(request,'deliveryboy/viewmywork.html',{'f':data})
def delivery(request):
    data=request.GET['proid']  
    sql="update buynow set status='2'where id='"+data+"'" 
    dbconnection.uprow(sql)
    return HttpResponseRedirect('delivery?proid='+data)
def completedwork(request) :
   em=request.session['us']
   sql="select * from buynow where status=2 and Deliveryboy='"+em+"'"
   data=dbconnection.selall(sql)
   return render(request,'deliveryboy/viewcmpltedwork.html',{'k':data})
def myoder(request):
    em=request.session['us']
    sql="select * from allproduct,buynow where allproduct.Id1=buynow.ProductId and (buynow.status=0 or buynow.status=1) and  buynow.Userid='"+em+"'"
    data=dbconnection.selall(sql)
    sql="select * from allproduct,buynow where allproduct.Id1=buynow.ProductId and (buynow.status=2)and  buynow.Userid='"+em+"'" 
    data1=dbconnection.selall(sql)
    return render(request,'user/myoder.html',{'l':data,'n':data1})

def deliverddetails(request):
    sql="select * from buynow where status=2"
    data=dbconnection.selall(sql)
    return render(request,'staff/vwdeliverddtls.html',{'o':data})


