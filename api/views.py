from django.http import JsonResponse
from django.shortcuts import render
from student.models import Student
from django.views.decorators.csrf import csrf_exempt
from .serializer import StudentSerializer


def index(request):

    return JsonResponse({'index':True})

def students(request):
    student = Student.objects.all()
    serialized = StudentSerializer(student,many=True)
    return JsonResponse({'success':True, 'students':serialized.data},safe=False)

def student_(request,id):
    try:
        student = Student.objects.get(id=id)    
        serialized = StudentSerializer(student,many=False)
        return JsonResponse({'success':True, 'data':serialized.data},safe=False)
    except Student.DoesNotExist:
        return JsonResponse({'success':False,'message':'student id doesnot exist'})
    

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        age = request.POST.get('age', '')

        if not name:
            return JsonResponse({'success':False,'message':'Please Provide Name'})
        if not email:
            return JsonResponse({'success':False,'message':'Please Provide Email'})
        if not age:
            return JsonResponse({'success':False,'message':'Please Provide Age'})
        Student.objects.create(name=name,email=email,age=age)
        return JsonResponse({'success':True, 'message':'User Created'})
    else:
        return render(request, 'index.html')

@csrf_exempt
def student_update(request):
    if request.method == 'POST':
        id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        age = request.POST.get('age', '')

        if not name:
            return JsonResponse({'success':False,'message':'Please Provide Name'})
        if not email:
            return JsonResponse({'success':False,'message':'Please Provide Email'})
        if not age:
            return JsonResponse({'success':False,'message':'Please Provide Age'})
        
        try:
            student = Student.objects.get(id=id)
            student.name = name
            student.email = email
            student.age = age
            student.save()
            return JsonResponse({'success':True, 'message':'Student Updated'})
        except Student.DoesNotExist:
            return JsonResponse({'success':False, 'message':'Student Id doesnot exist.'})


@csrf_exempt
def student_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id', '')
        if not id:
            return JsonResponse({'success':False,'message':'Please Provide student Id'})
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return JsonResponse({'success':True, 'message':'Student Deleted.'})
        except Student.DoesNotExist:
            return JsonResponse({'success':False, 'message':'Student not found.'})

    