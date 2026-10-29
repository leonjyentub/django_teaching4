from django.shortcuts import render

# Create your views here.
def home(request):
    name = '北商大'
    student = {
        'name': '小明',
        'age': 12,
        'gender': '男'
    }
    data = ['Python', 'Django', 'HTML', 'CSS', 'JavaScript']
    return render(request, 'pages/home.html', 
                  {'name': name, 
                   'stud': student,
                   'datas': data})
