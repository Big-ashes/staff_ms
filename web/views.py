from django.shortcuts import render, redirect
from web import models


# Create your views here.

def depart_list(request):
    """部门列表"""
    # 去数据表中获取所有部门列表
    # querset可以理解为一个列表
    queryset = models.Department.objects.all()

    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        return render(request, 'depart_add.html')

    # 获取用户通过POST提交的数据(title输入为空)
    title = request.POST.get("title")

    # 保存到数据库
    models.Department.objects.create(title=title)

    return redirect("/depart/list/")


def depart_delete(request):
    """删除部门"""
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


def depart_edit(request, nid):
    """修改部门"""
    # 根据数据，获取id的值[obj,]
    if request.method == "GET":
        row_obj = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'row_obj': row_obj})
        # print(row_obj.id, row_obj.title)
    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")


def user_list(request):
    """用户管理"""
    # 获取所有的用户列表
    queryset = models.UserInfo.objects.all()
    # for obj in queryset:
    # print(obj.id,obj.name,obj.password,obj.creat_time.strftime("%Y-%m-%d"),obj.get_gender_display())
    # print(obj.depart.title)
    return render(request, 'user_list.html', {'queryset': queryset})


def user_add(request):
    """添加用户(原始方式)"""
    if request.method == "GET":
        content = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all()
        }
        return render(request, "user_add.html", content)
    # 获取用户提交的数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gd')
    depart_id = request.POST.get('dp')
    # 添加到数据库

    models.UserInfo.objects.create(name=user, password=pwd, age=age, account=account, creat_time=ctime, gender=gender,
                                   depart_id=depart_id)

    # 返回到用户界面
    return redirect("/user/list/")
