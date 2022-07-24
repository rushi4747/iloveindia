from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = (
    path("", views.index, name="homepage"),
    path("registeruser", views.registeruser, name="registeruser"),
    path("registerorg", views.registerorg, name="registerorg"),
    path("registercust", views.registercust, name="registercust"),

    path("about", views.about, name="aboutus"),
    path("contact", views.contact, name="contact"),
    path("giveadd", views.giveadd, name="giveadd"),
    path("uploadjob", views.uploadjob, name="uploadjob"),
    path("payment", views.payment, name="payment"),
    path("news", views.news, name="news"),
    path("jobportal", views.jobportal, name="jobportal"),
    path("place", views.place, name="place"),
    path("entertainment", views.entertainment, name="entertainment"),
    path("education", views.education, name="education"),
    path("newsdetail<int:newsid>", views.newsdetail, name="newsdetail"),
    path("placedetail<int:placeid>", views.placedetail, name="placedetail"),
    path("logincheck", views.logincheck, name="logincheck"),
    path("videos", views.videos, name="videos"),



    path("userprofile", views.userprofile, name="userprofile"),
    path("logout", views.logout, name="logout"),
    path("getuser", views.userno, name="getuser"),

    path("adminlogin", views.adminlogin, name="adminlogin"),
    path("adlogout", views.adlogout, name="adlogout"),

    # path for Editor site
    path("editorhome", views.editorindex, name="editorhome"),
    path("managenews", views.managenews, name="managenews"),
    path("deletenews<int:nid>", views.deletenews, name="deletenews"),

    path("managejob", views.managejob, name="managejob"),
    path("manageplace", views.manageplace, name="manageplace"),
    path("manageeducational", views.manageeducational, name="manageeducational"),
    path("manageentertainment", views.manageentertainment, name="manageentertainment"),
    path("managevideo", views.managevideo, name="managevideo"),

    # path for admin site
    path("adminhome", views.adminindex, name="adminhome"),
    path("observeeditor", views.observeeditor, name="observeeditor"),
    path("approveadd", views.approveadd, name="approveadd"),

)
