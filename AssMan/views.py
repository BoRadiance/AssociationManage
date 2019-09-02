from django.shortcuts import render,redirect
from django.forms import ModelForm
from .models import Article,Depart,People
from django.forms import widgets as wid

# Create your views here.

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        labels ={'title':"新闻标题",'content':"新闻内容",'date':'发布时间'}
        widgets ={
            "title": wid.TextInput(attrs={"class": "form-control"}),
            "date": wid.TextInput(attrs={"class": "form-control"}),
            "content": wid. Textarea(attrs={'cols': 80, 'rows': 20,"class": "form-control"}), # 关键是这一行),
        }
        error_messages = {
            "title": {"required": "不能为空"},
            "content": {"required": "不能为空"},
            "date": {"required": "不能为空"},
        }


class DepartForm(ModelForm):
    class Meta:
        model = Depart
        fields = "__all__"

        widgets = {
            "title": wid.TextInput(attrs={"class": "form-control"}),
            "desc": wid.TextInput(attrs={"class": "form-control"}),
        }
        error_messages = {
            "title": {"required": "不能为空"},
            "desc": {"required": "不能为空"},
        }


class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = "__all__"

        widgets = {
            "name":wid.TextInput(attrs={"class": "form-control"}),
            "sex":wid.TextInput(attrs={"class": "form-control"}),
            "depart":wid.Select(attrs={"class": "form-control"}),
        }

        error_messages={
            "name": {"required": "不能为空"},
            "sex":{"required": "不能为空"},
            "depart":{"required": "不能为空"},
        }


def showarticle(request):
    article_list = Article.objects.all()
    print(article_list)
    return render(request,"index.html",locals())


def admindepart(request):
    depart_list = Depart.objects.all()
    return render(request,"departadmin.html",locals())

def adminpeople(request):
    people_list = People.objects.all()
    return render(request,"peopleadmin.html",locals())

def adminarticle(request):
    article_list = Article.objects.all()
    return render(request, "associationadmin.html", locals())


def addarticle(request):
    if request.method =="POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/adminarticle")

    form = ArticleForm()
    return render(request,"add_article.html",locals())


def adddepart(request):
    if request.method == "POST":
        form = DepartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/admindepart")

    form = DepartForm()
    return render(request, "add_depart.html", locals())


def addpeople(request):
    if request.method == "POST":
        form = PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/adminpeople")

    form = PeopleForm()
    return render(request, "add_people.html", locals())


def articledetail(request,pid):
    articledet = Article.objects.get(id=pid)

    return render(request,"detail.html",locals())

def delarticle(request,pid):
    art = Article.objects.get(id=pid)
    art.delete()

    return redirect("/adminarticle")

def editarticle(request,pid):
    edit_article = Article.objects.filter(id=pid).first()
    if request.method == "POST":
        form = ArticleForm(request.POST,instance=edit_article)
        if form.is_valid():
            form.save()
            return redirect("/adminarticle")

    form = ArticleForm()
    return render(request, "edit_article.html", locals())


def deldepart(request,pid):
    art = Depart.objects.get(id=pid)
    art.delete()
    return redirect("/admindepart")

def editdepart(request,pid):
    edit_article = Depart.objects.filter(id=pid).first()
    if request.method == "POST":
        form = DepartForm(request.POST,instance=edit_article)
        if form.is_valid():
            form.save()
            return redirect("/admindepart")

    form = DepartForm()
    return render(request, "edit_depart.html", locals())


def delpeople(request,pid):
    art = People.objects.get(id=pid)
    art.delete()
    return redirect("/adminpeople")


def editpeople(request,pid):
    edit_article = People.objects.filter(id=pid).first()
    if request.method == "POST":
        form = PeopleForm(request.POST, instance=edit_article)
        if form.is_valid():
            form.save()
            return redirect("/adminpeople")

    form = PeopleForm()
    return render(request, "edit_people.html", locals())



