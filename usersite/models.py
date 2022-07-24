from django.db import models
import datetime
# Create your models here.
class Customer(models.Model):
    Cid=models.AutoField
    Business_Name= models.CharField(max_length=30, default="")
    Address = models.CharField(max_length=50, default="")
    Customer_Name =models.CharField(max_length=30, default="")
    Mobile_No =models.CharField(max_length=10, default="")
    Email = models.EmailField(max_length=50)
    Username =models.CharField(max_length=30, default="")
    Password =models.CharField(max_length=30, default="")

    def __str__(self):
        return self.Customer_Name

class User(models.Model):
    Uid=models.AutoField
    First_Name= models.CharField(max_length=10, default="")
    Last_name = models.CharField(max_length=10, default="")
    Age = models.CharField(max_length=10, default="")
    Gender =models.CharField(max_length=30, default="")
    Mobile_No = models.CharField(max_length=10, default="")
    Email = models.EmailField(max_length=50)
    Username =models.CharField(max_length=30, default="")
    Password =models.CharField(max_length=30, default="")

    def __str__(self):
        return self.First_Name

class Organization(models.Model):
    Company_Id=models.AutoField
    Company_Name= models.CharField(max_length=30, default="")
    Address = models.CharField(max_length=50, default="")
    Owner_name= models.CharField(max_length=30, default="")
    Mobile_No= models.CharField(max_length=10, default="")
    Email = models.EmailField(max_length=50)
    Username  = models.CharField(max_length=30, default="")
    Password  = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.Company_Name

class News(models.Model):
    News_Id=models.AutoField
    Headline= models.CharField(max_length=200, default="")
    Img1= models.ImageField(upload_to="usersite/newsimg", default="")
    News_Disc= models.CharField(max_length=1000, default="")
    ndate=models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.Headline

class Job_Portal(models.Model):
    Job_Id=models.AutoField
    Company_Name= models.CharField(max_length=30, default="")
    Date= models.DateField(default=datetime.date.today)
    Job_Disc= models.CharField(max_length=1000, default="")
    Company_Email= models.EmailField(max_length=50,default="")
    Mobile_No= models.CharField(max_length=30, default="")
    link= models.CharField(max_length=200, default="")

    def __str__(self):
        return self.Company_Name

class Place(models.Model):
    Place_Id=models.AutoField
    Place_Name= models.CharField(max_length=30, default="")
    Dist= models.CharField(max_length=30, default="")
    Img1= models.ImageField(upload_to="usersite/placeimg", default="")
    Img2= models.ImageField(upload_to="usersite/placeimg", default="")
    Place_Disc= models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.Place_Name

class Educational(models.Model):
    Edu_Id=models.AutoField
    Header= models.CharField(max_length=100, default="")
    Img= models.ImageField(upload_to="usersite/placeimg", default="")
    Edu_Disc= models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.Header


class Entertainment(models.Model):
    Ent_Id=models.AutoField
    Section= models.CharField(max_length=30, default="")
    Header= models.CharField(max_length=100, default="")
    Img= models.ImageField(upload_to="usersite/Entimg", default="")
    Ent_Desc= models.CharField(max_length=500, default="")

    def __str__(self):
        return self.Header

class Video(models.Model):
    Vid_Id=models.AutoField
    Title= models.CharField(max_length=100, default="")
    Video= models.ImageField(upload_to="usersite/Videos", default="")
    Vid_Desc= models.CharField(max_length=500, default="")

    def __str__(self):
        return self.Title

class Feedback(models.Model):
    F_Id=models.AutoField
    Feedback= models.CharField(max_length=500, default="")
    deleted= models.BooleanField(default=True)

    def __str__(self):
        return self.F_Id

class E_Notification(models.Model):
    N_Id=models.AutoField
    N_disc= models.CharField(max_length=100, default="")

    def __str__(self):
        return self.N_Id


class Advertisement(models.Model):
    A_Id=models.AutoField
    Header= models.CharField(max_length=100, default="")
    img= models.ImageField(upload_to="usersite/adimg", default="")
    Disc= models.CharField(max_length=500, default="")
    Mobile_No= models.IntegerField(default=0)
    Email= models.EmailField(max_length=50)
    Duration=models.CharField(max_length=30, default="")
    Key= models.BooleanField(default=True)

    def __str__(self):
        return self.Header


class Payment(models.Model):
    P_Id= models.AutoField
    Cid= models.IntegerField(default=0)
    Aid= models.IntegerField(default=0)
    Date= models.DateField()
    Amount= models.IntegerField(default=0)

    def __str__(self):
        return self.P_Id


class Info_User(models.Model):
    Info_Id= models.AutoField
    Section= models.CharField(max_length=30, default="")
    Header= models.CharField(max_length=100, default="")
    Img= models.ImageField(upload_to="usersite/UserUploadimg", default="")
    info_disc= models.CharField(max_length=1000, default="")
    Approve= models.BooleanField(default=False)

    def __str__(self):
        return self.Header


class Upload_Job(models.Model):
    Job_Id= models.AutoField
    Job_disc= models.CharField(max_length=500, default="")
    Email= models.EmailField(max_length=50)
    Mobile= models.IntegerField(default=10)

    def __str__(self):
        return self.Job_Id

class Slider_Img(models.Model):
    Img_Id= models.AutoField
    Img_Name= models.CharField(max_length=50, default="")
    Img= models.ImageField(upload_to="usersite/slider", default="")

    def __str__(self):
        return self.Img_Name

#table for get user whats app no and name
class getuser(models.Model):
    Uid=models.AutoField
    Name= models.CharField(max_length=20, default="")
    Mobile= models.IntegerField(default=10)

    def __str__(self):
        return self.Name