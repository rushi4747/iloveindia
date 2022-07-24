from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider_Img, News, Advertisement, Job_Portal, Place, User, Organization, Customer, getuser, Entertainment, Educational
from django.contrib import messages

# Create your views here.

def index(request):
    slider_img= Slider_Img.objects.all()
    newsinfo= News.objects.all().order_by('-id')[:4]
    ad= Advertisement.objects.all().order_by('-id')[:1]
    
    n=len(slider_img)
    params={'slideimg':slider_img,'newsinfo':newsinfo ,'ad':ad,'range':range(n),'j':1}
    return render(request,'usersite/index.html',params)


def news(request):
    newsinfo= News.objects.all().order_by('-id')[:4]
    params={'newsinfo':newsinfo}
    return render(request,'usersite/News.html',params)

def newsdetail(request, newsid):
    news= News.objects.filter(id=newsid)
    params={'news':news[0]}
    return render(request,'usersite/newsdetail.html',params)


def jobportal(request):
    jobinfo= Job_Portal.objects.all()
    params={'jobinfo':jobinfo}
    return render(request,'usersite/jobportal.html',params)

def uploadjob(request): #method for upload job for org
    if request.method =="POST":
        if request.POST.get('cname'):
            cname=request.POST.get('cname','')
            cdate=request.POST.get('cdate','')
            cdisc=request.POST.get('cdisc','')
            cemail=request.POST.get('cemail','')
            cmob=request.POST.get('cmob','')
            clink=request.POST.get('clink','')
            uploadjob=Job_Portal(Company_Name=cname, Date=cdate, Job_Disc=cdisc, Company_Email=cemail, Mobile_No=cmob,link=clink)
            uploadjob.save()
            messages.info(request,'Job Upload succesfully!')
    return render(request,'usersite/uploadjob.html')

def place(request):
    placeinfo= Place.objects.all()
    params={'placeinfo':placeinfo}
    return render(request,'usersite/place.html',params)

def entertainment(request):
    entertain= Entertainment.objects.all()
    params={'entertain':entertain}
    return render(request,'usersite/entertainment.html',params)

def education(request):
    education= Educational.objects.all()
    params={'education':education}
    return render(request,'usersite/education.html',params)

def placedetail(request, placeid):
    place= Place.objects.filter(id=placeid)
    params={'place':place[0]}
    return render(request,'usersite/placedetail.html',params)

def registeruser(request):
    if request.method =="POST":
        print('org registration')
        name= request.POST.get('name','')
        surname= request.POST.get('surname','')
        age= request.POST.get('age','')
        gender= request.POST.get('gender','')
        mobile= request.POST.get('mobile','')
        email= request.POST.get('email','')
        username= request.POST.get('username','')
        password= request.POST.get('password','')

        reguser=User(First_Name=name, Last_name=surname, Age=age, Gender=gender, Mobile_No=mobile, Email=email, Username=username, Password=password)
        reguser.save()
        
        messages.info(request, name+' welcome to ILoveIndia family!')
        return HttpResponse(index(request))
    return render(request,'usersite/register.html')
    
def registerorg(request):
    if request.method =="POST":
        print('user registration')
        Company_Name= request.POST.get('cname','')
        Address= request.POST.get('address','')
        Owner_Name= request.POST.get('onername','')
        Mobile_No= request.POST.get('mobile','')
        Email= request.POST.get('email','')
        Username= request.POST.get('username','')
        password= request.POST.get('password','')

        regorg=Organization(Company_Name=Company_Name, Address=Address, Owner_name=Owner_Name, Mobile_No=Mobile_No, Email=Email, Username=Username, Password=password)
        regorg.save()
        messages.info(request, Owner_Name+' Welcome to ILoveIndia Family!')
        return HttpResponse(index(request))
    return render(request,'usersite/register.html')

def registercust(request):
    if request.method =="POST":
        Business_Name= request.POST.get('bname','')
        Address= request.POST.get('address','')
        Customer_Name= request.POST.get('cname','')
        Mobile_No= request.POST.get('mobile','')
        Email= request.POST.get('email','')
        username= request.POST.get('username','')
        password= request.POST.get('password','')

        regcust=Customer(Business_Name=Business_Name, Address=Address, Customer_Name=Customer_Name, Mobile_No=Mobile_No, Email=Email, Username=username, Password=password)
        regcust.save()
        messages.info(request, Customer_Name+' Welcome to ILoveIndia Family!')
        return HttpResponse(index(request))
    return render(request,'usersite/register.html')

def about(request):
    return render(request,'usersite/aboutus.html')

def videos(request):
    return render(request,'usersite/videos.html')

def contact(request):
    
    return render(request,'usersite/contactus.html')

def giveadd(request):
    return render(request,'usersite/giveadd.html')
    
def payment(request):
    if request.method =="POST":
        request.session["aduname"]=request.POST.get('name','')
        request.session["adweek"]=request.POST.get('week','')
        request.session['adamt']=int(request.POST.get('week',''))*5000
        return render(request,'usersite/payment.html')



def logincheck(request):    #check login
    if request.method =="POST":
        user=request.POST.get('options','')
        uname=request.POST.get('uname','')
        password=request.POST.get('password','')

        if user=='user':
            Userlog= User.objects.filter(Username=uname,Password=password)
            if Userlog:
                for e in Userlog:
                    request.session["role"] = "user"
                    request.session["id"] = e.id
                    request.session["Username"] = e.Username
                messages.info(request,'Login Successfully!')
                return HttpResponse(index(request))
            else:
                messages.info(request,'Wrong uname password or your role!!')
                return HttpResponse(index(request))

        if user=='org':
            Userlog= Organization.objects.filter(Username=uname,Password=password)
            if Userlog:
                for e in Userlog:
                    request.session["role"] = "org"
                    request.session["id"] = e.id
                    request.session["Username"] = e.Username
                messages.info(request,'Login Successfully!')
                return HttpResponse(index(request))
            else:
                messages.info(request,'Wrong uname password or your role!!')
                return HttpResponse(index(request))
        
        if user=='cust':
            Userlog= Customer.objects.filter(Username=uname,Password=password)
            if Userlog:
                for e in Userlog:
                    request.session["role"] = "cust"
                    request.session["id"] = e.id
                    request.session["Username"] = e.Username
                messages.info(request,'Login Successfully!')
                return HttpResponse(index(request))
            else:
                messages.info(request,'Wrong uname password or your role!!')
                return HttpResponse(index(request))

def userprofile(request): #function for manage user/org/cust profile
    if request.session["role"]=="user":
        user= User.objects.filter(id=request.session["id"])
        params={'userdetail':user}
        return render(request,'usersite/userprofile.html',params)
    
    if request.session["role"]=="org":
        org= Organization.objects.filter(id=request.session["id"])
        params={'userdetail':org}
        return render(request,'usersite/orgprofile.html',params)

    if request.session["role"]=="cust":
        cust= Customer.objects.filter(id=request.session["id"])
        params={'userdetail':cust}
        return render(request,'usersite/custprofile.html',params)

def logout(request):
    if request.method =="GET":
        del request.session["role"]
        del request.session["id"]
        del request.session["Username"]
        messages.info(request,'LogOut successfully!!')
        return HttpResponse(index(request))

def userno(request): #method is use for get user whatsapp no
    if request.method =="POST":
        name= request.POST.get('name','')
        mobile= request.POST.get('mobile','')
        
        regcust=getuser(Name=name, Mobile=mobile)
        regcust.save()
        messages.info(request,' We got your whatsapp number successfully!!')
        return HttpResponse(index(request))



def adminlogin(request): #method is use for login for admin and editor
    if request.method =="POST":
        user=request.POST.get('options','')
        uname=request.POST.get('username','')
        password=request.POST.get('password','')

        if user=='admin' and uname=='rushi' and password=='4747':
            request.session["adrole"] = user
            request.session["adusername"] = uname
            messages.info(request,'Welcome Admin!')
            return render(request,'adminsite/adminhome.html')
        elif user=='editor' and uname=='tushar' and password=='123':
            request.session["adrole"] = user
            request.session["adusername"] = uname
            messages.info(request,'Welcome Editor!')
            return render(request,'editorsite/editorhome.html')
        else:
            messages.info(request,'Wrong uname password or your role!!')
            return render(request,'adminlogin.html')
    return render(request,'adminlogin.html')

def adlogout(request): #method for admin logout
    if request.method =="GET":
        if request.session["adrole"]=="admin":
             messages.info(request,'Welcome back Admin,.logout!!')
        else:
             messages.info(request,'Welcome back Editor,.logout!!')
        del request.session["adrole"]
        del request.session["adusername"]
       
        return render(request,'adminlogin.html')

#admin site functions!!!
def adminindex(request):
    return render(request,'adminsite/adminhome.html')

def observeeditor(request):
    return render(request,'adminsite/observeeditor.html')

def approveadd(request):
    return render(request,'adminsite/approveadd.html')

#Editor site functions!!!
def editorindex(request):
    return render(request,'editorsite/editorhome.html')

def managenews(request): #method for manage news
    if request.method =="POST":
        if request.POST.get('nheadline'):
            nheadline=request.POST.get('nheadline','')
            nimg=request.FILES['nimg']
            ndisc=request.POST.get('ndisc','')
            uploadnews=News(Headline=nheadline, Img1=nimg, News_Disc=ndisc)
            uploadnews.save()
            messages.info(request,'News Upload succesfully!')

        if request.POST.get('sdate'):
            sdate=request.POST.get('sdate')
            edate=request.POST.get('edate')
            request.session["sdate"] = sdate
            request.session["edate"] = edate
            sresult= News.objects.filter(ndate__range=[sdate,edate])
            params={'sresult':sresult,'show':"show"}
            return render(request,'editorsite/managenews.html',params)

    return render(request,'editorsite/managenews.html')

def deletenews(request, nid):  #function for delete news by id
    News.objects.filter(id=nid).delete()
    sresult= News.objects.filter(ndate__range=[request.session['sdate'],request.session['edate']])
    messages.info(request,'News Deleted succesfully!')
    params={'sresult':sresult,'show':"show"}
    return render(request,'editorsite/managenews.html',params)

def managejob(request):
    if request.method =="POST":
        if request.POST.get('cname'):
            cname=request.POST.get('cname','')
            cdate=request.POST.get('cdate','')
            cdisc=request.POST.get('cdisc','')
            cemail=request.POST.get('cemail','')
            cmob=request.POST.get('cmob','')
            clink=request.POST.get('clink','')
            uploadjob=Job_Portal(Company_Name=cname, Date=cdate, Job_Disc=cdisc, Company_Email=cemail, Mobile_No=cmob,link=clink)
            uploadjob.save()
            messages.info(request,'Job Upload succesfully!')

        if request.POST.get('sdate'):
            sdate=request.POST.get('sdate')
            edate=request.POST.get('edate')
            request.session["sdate"] = sdate
            request.session["edate"] = edate
            sresult= Job_Portal.objects.filter(Date__range=[sdate,edate])
            params={'sresult':sresult,'show':"show"}
            return render(request,'editorsite/managejob.html',params)
    return render(request,'editorsite/managejob.html')

def manageplace(request):
    if request.method =="POST":
        messages.info(request,'Placeinfo Upload succesfully!')
    return render(request,'editorsite/manageplace.html')

def manageeducational(request):
    if request.method =="POST":
        messages.info(request,'Educationalinfo Upload succesfully!')
    return render(request,'editorsite/manageeducational.html')

def manageentertainment(request):
    if request.method =="POST":
        messages.info(request,'Entertainment Upload succesfully!')
    return render(request,'editorsite/manageentertainment.html')

def managevideo(request):
    if request.method =="POST":
        messages.info(request,'Video Upload succesfully!')
    return render(request,'editorsite/managevideo.html')
    