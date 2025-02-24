from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import log,register

# Create your views here.
def login_page(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        upwd=request.POST.get("upwd")

        if log.objects.filter(uname=uname,upwd=upwd):
            l=log.objects.get(uname=uname,upwd=upwd)

            if l.utype=="student":
                request.session["uid"]=l.uid_id
                return HttpResponse("<script>alert('welcome student');window.location='/student';</script>")
            elif l.utype=="staff":
                
                request.session["uid"]=l.uid_id
                return HttpResponse("<script>alert('welcome user');window.location='/staff_p';</script>")


            elif l.utype=="admin":
                return HttpResponse("<script>alert('welcome admin');window.location='/a_page';</script>")
            else:
                return HttpResponse("<script>alert('invalid');window.location='/log';<script>")

        else:
            return HttpResponse("<script>alert('invalid');window.location='/log';<script>")  

    else: 
        template=loader.get_template("login.html")
        context={}
        return HttpResponse(template.render(context,request))



def home_page(request):
    template=loader.get_template("home.html")
    context={}
    return HttpResponse(template.render(context,request))
def form_page(request):
    if request.method == 'POST':
        r=register()
        r.name=request.POST.get("name")
        r.gender=request.POST.get("gender")
        r.phone=request.POST.get("phone")
        r.email=request.POST.get("email")
        r.img=request.FILES["photo"]
        r.save()
        id=register.objects.latest("id").id

        l=log()
        l.uname=request.POST.get("uname")
        l.upwd=request.POST.get("pwd")
        l.utype=request.POST.get("utype")
        l.uid_id=id
        l.save()
        return HttpResponse("<script>alert('inserted');window.location='/reg';</script>")
  
    else:
        
        template=loader.get_template("register.html")
        context={}
        return HttpResponse(template.render(context,request))


def admin_page(request):
    template=loader.get_template("admin.html")
    context={}
    return HttpResponse(template.render(context,request))
def aview_page(request):
    d=register.objects.all()
    template=loader.get_template("admin_view.html")
    context={'data':d}
    return HttpResponse(template.render(context,request))
def delete(request,id):
    data=register.objects.get(id=id)
    l=log.objects.get(uid_id=id)
    data.delete()
    l.delete()
    return HttpResponse("<script>alert('d_user');window.location='/a_view';</script>")




def student_page(request):
    template=loader.get_template("student.html")
    context={}
    return HttpResponse(template.render(context,request))
def studview_page(request):
    d=register.objects.raw("select*from app1_register where id=%s",[request.session["uid"]])
    template=loader.get_template("student_view.html")
    context={'data':d }
    return HttpResponse(template.render(context,request))    




def staff_page(request):
    template=loader.get_template("staff.html")
    context={}
    return HttpResponse(template.render(context,request))
def sview_page(request):
    d=register.objects.raw("select*from app1_register where id=%s",[request.session["uid"]])
    template=loader.get_template("staff_view.html")
    context={'data':d }
    return HttpResponse(template.render(context,request))    
def edit_detail(request):
    if request.method=="POST":
        r=register.objects.get(id=request.session["uid"])
        r.name=request.POST.get("name")
        r.gender=request.POST.get("gender")
        r.email=request.POST.get("email")
        r.phone=request.POST.get("phone")
        r.save()
        return HttpResponse("<script>alert('edited');window.location='/detail';</script>")
    else:
        u=register.objects.get(id=request.session["uid"])
        template=loader.get_template("edit.html")
        context={'u':u}
        return HttpResponse(template.render(context,request))
def stud_detail(request):
    d=register.objects.raw("select * from app1_register,app1_log where app1_register.id=app1_log.uid_id and app1_log.utype=%s",['student'])
    template=loader.get_template("stud_staff.html")
    context={'data':d }
    return HttpResponse(template.render(context,request))