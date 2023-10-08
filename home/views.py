from django.shortcuts import render
from django.http import HttpResponse
from home.forms import studentForm,infoForm
from home.models import student
from django.db import connection

# Create your views here.
def home(request):
    dict = []
    x = {"Name":"Akash","Prof":"Teacher"}
    dict.append(x)
    x = {"Name":"Shamim","Prof":"Student"}
    dict.append(x)
    return render(request,'demo.html',{"Users":dict})

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def StudentForm(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        form.save()
        return HttpResponse("<h1>Success</h1>")
    else:
        form = studentForm
        return render(request,'input.html',{"form":form})

# def getInfo(request):
#     pupil = student.objects.get(pk=5)
#     pupil.Name = 'Yeamin'
#     pupil.save()
#     all_students = student.objects.all()
#     return render(request,'infoViewer.html',{'students':all_students})

def getInfo(request):
    cursor = connection.cursor()
    sql = "SELECT * FROM STUDENT "
    cursor.execute(sql)
    result = cursor.fetchall()
    all_students = []
    for row in result:
        name = row[1]
        clas = row[2]
        roll = row[3]
        one = {'Name':name,'Class':clas,'Roll':roll}
        all_students.append(one)
    return render(request,"infoViewer.html",{"students":all_students})
