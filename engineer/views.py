import json
from django.shortcuts import render
from django.http import JsonResponse
from engineer.models import Engineer

# Create your views here.
# 增加工程师
def add_engineer(request):


    if request.method == 'POST':
        name = request.GET.get('name')
        age = request.GET.get('age')
        phone_number = request.GET.get('phone_number')
        # specialty = request.POST.get('specialty')
        engineer = Engineer(name=name, age=age, phone_number=phone_number)
        engineer.save()
        return JsonResponse({'message': '工程师添加成功'})

# 删除工程师
def delete_engineer(request):
    if request.method == 'POST':
        try:
            engineer = Engineer.objects.get(id=request.GET.get('id'))
            engineer.delete()
            return JsonResponse({'message': '工程师删除成功'})
        except Engineer.DoesNotExist:
            return JsonResponse({'message': '工程师不存在'}, status=404)

# 查询工程师
def get_engineer(request):
    if request.method == 'GET':
        try:
            engineer = Engineer.objects.get(id=request.GET.get('id'))
            data = {
                'id': engineer.id,
                'name': engineer.name,
                'age': engineer.age,
                'phone_number': engineer.phone_number,
            }
            return JsonResponse(data)
        except Engineer.DoesNotExist:
            return JsonResponse({'message': '工程师不存在'}, status=404)

# 更新工程师
def update_engineer(request):
    if request.method == 'POST':
        try:
            engineer = Engineer.objects.get(id=request.GET.get('id'))
            name = request.GET.get('name', engineer.name)
            age = request.GET.get('age', engineer.age)
            phone_number = request.GET.get('phone_number', engineer.phone_number)
            # specialty = request.PUT.get('specialty', engineer.specialty)
            engineer.name = name
            engineer.age = age
            engineer.phone_number = phone_number
            # engineer.specialty = specialty
            engineer.save()
            return JsonResponse({'message': '工程师更新成功'})
        except Engineer.DoesNotExist:
            return JsonResponse({'message': '工程师不存在'}, status=404)



# 获取所有工程师
def get_all_engineers(request):
    if request.method == 'GET':
        engineers = Engineer.objects.all()
        data = [
            {
                'id': engineer.id,
                'name': engineer.name,
                'age': engineer.age,
                'phone_number': engineer.phone_number,
            }
    for engineer in engineers
    ]
    return JsonResponse(data, safe=False)
def demo(request):
    return JsonResponse({'message': 'Hello, world!'})