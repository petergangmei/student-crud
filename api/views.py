from django.http import JsonResponse
from student.models import Stuent
from django.views.decorators.csrf import csrf_exempt


def index(request):

    return JsonResponse({'index':True})

def students(request):

    return JsonResponse({'students':True})

def student_(request,id):

    return JsonResponse({'students':True})

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '')
        age = request.POST.get('age', '')

        if not name:
            return JsonResponse({'message':'Please Provide Name'})
        if not email:
            return JsonResponse({'message':'Please Provide Email'})
        if not age:
            return JsonResponse({'message':'Please Provide Age'})
        Stuent.objects.create(name=name,email=email,age=age)
        return JsonResponse({'students created':True})

@csrf_exempt
def student_update(request):

    return JsonResponse({'student updat':True})


@csrf_exempt
def student_delete(request):

    return JsonResponse({'students delete':True})