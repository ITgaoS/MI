from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from Backstage.models import *
from Muser.models import *

import hashlib,re
def valid_user(email):
    try:
        user=User.objects.get(email=email)
    except Exception as e:
        return False
    else:
        return user
# Create your views here.
def valid_login(fun):
    def inner(request,*args,**kwargs):
        cookie_email=request.COOKIES.get("email")
        session_email=request.session.get("email")
        if cookie_email and session_email and cookie_email==session_email:
            return fun(request,*args,**kwargs)
        else:
            return  HttpResponseRedirect("/Backstage/login/")
    return inner

def set_password(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result
def register(request):
    if request.method=="POST":
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        gender=request.POST.get("gender")
        user=User()
        user.gender=gender
        user.username=username
        user.email=email
        user.password=set_password(password)
        user.save()
    return render(request, "backstage/signup.html")
def login(request):
    error=""
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            user=User.objects.get(email=email)
            if user.password==set_password(password) :
                response=HttpResponseRedirect("/Backstage/index/")
                response.set_cookie("email",user.email)
                request.session["email"]=user.email
                return response
            else:
                error="密码错误"
        except:
            error="用户名不存在"
    return  render(request,"backstage/login.html",locals())
def logout(request):
    response=HttpResponseRedirect("/Backstage/login/")
    response.delete_cookie("email")
    request.session.clear()
    return response
def forget_password(request):
    error=""
    if request.method == 'POST':
        email_post = request.POST.get("email")
        try:
            email = User.objects.get(email=email_post)
            if email:
                hash_code = set_password(email_post)
                contecnt = "http://127.0.0.1:8000/Backstage/change_password/?email=%s&token=%s" % (email_post, hash_code)
                print(contecnt)
                error="已发入您的邮箱  请查看修改密码！！！"
        except:
            pass

    return render(request,"backstage/forget_password.html",locals())
def reset_password(request):
    pass

def change_password(request):
    error=""
    if request.method == "POST":
        email = request.COOKIES.get("change_email")
        password = request.POST.get("password")
        e = User.objects.get(email=email)
        e.password = set_password(password)
        e.save()
        return HttpResponseRedirect("/Backstage/login/")
    # 通过get请求获得了修改密码的用户和校验值
    email = request.GET.get("email")
    token = request.GET.get("token")
    # 进行再次校验
    now_token = set_password(email)
    # 当前提交人存在，并且token值正确
    if valid_user(email) and now_token == token:
        # 返回修改密码页面
        reponse = render(request, "backstage/change_password.html", locals())
        reponse.set_cookie("change_email",email)
        return reponse
    else:
        return HttpResponseRedirect("/Backstage/forget_password/")
@valid_login
def index(request):
    return render(request,"backstage/index.html")
@valid_login
def add_comm(request):
    type_list=CommodityType.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        price=request.POST.get("price")
        specification=request.POST.get("specification")
        color=request.POST.get("color")
        type=request.POST.get("type")
        picture=request.FILES.get("picture")
        comm=Goods()
        comm.name=name
        comm.price=price
        comm.specification=specification
        comm.color=color
        comm.type=CommodityType.objects.get(id=type)
        if picture:
            comm.picture=picture
        comm.save()
    return render(request,"backstage/add_comm.html",locals())
@valid_login
def self_info(request):
    email=request.COOKIES.get("email")
    try:
        user=User.objects.get(email=email)
    except:
        pass
    return render(request,"backstage/self_info.html",locals())
@valid_login
def edit_self_info(request):
    email = request.COOKIES.get("email")
    user = User.objects.get(email=email)
    if request.method=="POST":
        email=request.POST.get("email")
        username=request.POST.get("username")
        gender=request.POST.get("gender")
        phone=request.POST.get("phone")
        age=request.POST.get("age")
        address=request.POST.get("address")
        picture=request.FILES.get("picture")


        if gender=="男":
            gender=1
        elif gender == "女":
            gender =0
        user.email=email
        user.username=username
        user.age=age
        user.gender=gender
        user.phone=phone
        user.address=address
        if picture:
            user.picture=picture
        user.save()
    return  render(request,"backstage/edit_self_info.html",locals())
def comm_list(request):
    id=request.GET.get("id")
    status=request.GET.get("status")
    number=request.GET.get("page",1)
    try:
        comm=Goods.objects.get(id=id)
        if status=="up":
            comm.state=1
        elif status=="down":
            comm.state=0
        comm.save()
    except:
        pass

    comm_list=Goods.objects.all().order_by("-state")
    page_data=Paginator(comm_list,20)
    page_list=page_data.page(number)
    page_range = list(page_data.page_range)
    num = len(page_range)
    if int(number)<2:
        page_range=[1,2,3,4,5]
    elif int(number)>=3:
        page_range=page_range[int(number)-3:int(number)+3]
    elif int(number)+4==num:
        page_range=page_range[-6:]

    print(page_range)
    return render(request,"backstage/comm_list.html",locals())




def add(request):
    C=Goods.objects.all()

    print(C)
    for i in C :
        i.picture=i.picture.url.replace("/media","")
        print(i.picture)
        i.save()
    # import random
    # import json
    # with open(r'E:\python_lrean\Django\MI\MI\Backstage\data3.json','r',encoding="utf-8")as f:
    #     data=f.read()
    # data=json.loads(data)
    # i=1
    # for da in data:
    #
    #     for  d in da:
    #         comm=Goods()
    #         comm.name=d["title"]
    #         comm.price=d['price']
    #
    #         comm.specification=d['title']
    #         comm.state=1
    #         comm.vers=d['title']
    #         comm.picture='backstage/images'+d['img'].split('/')[-1]
    #         comm.type=CommodityType.objects.get(id=i+1)
    #         pattern = re.compile(' ([\u4e00-\u9fa5]*?["红"|"黑"|"白"|"蓝"|"橙"|"绿"|"紫"|"靑"|"黄"|"色"])')
    #         try:
    #             colors=pattern.findall(d['title'])[0]
    #             comm.color = colors
    #         except:
    #             comm.color='标准色'
    #         print(comm.color)
    #         comm.save()
    #     i+=1


    return HttpResponse('hello')