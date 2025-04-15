from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from workorder.models import WorkOrder
import json

# 创建工单
def create_workorder(request):
    if request.method == 'POST':
        try:
            # 从请求体中解析 JSON 数据
            data = json.loads(request.body)
            # 创建新的工单
            workorder = WorkOrder.objects.create(**data)
            return JsonResponse({'message': '工单创建成功', 'id': workorder.id}, status=201)
        except Exception as e:
            # 返回错误信息
            return JsonResponse({'error': str(e)}, status=400)
    # 如果请求方法不是 POST，返回 405 错误
    return JsonResponse({'error': '无效的请求方法'}, status=405)

# 查询工单
def retrieve_workorder(request, workorder_id):
    if request.method == 'GET':
        # 根据 ID 查询工单，如果不存在则返回 404
        workorder = get_object_or_404(WorkOrder, id=workorder_id)
        # 返回工单数据
        return JsonResponse({'id': workorder.id, 'data': workorder.data}, status=200)
    # 如果请求方法不是 GET，返回 405 错误
    return JsonResponse({'error': '无效的请求方法'}, status=405)

# 更新工单
def update_workorder(request, workorder_id):
    if request.method == 'PUT':
        try:
            # 根据 ID 查询工单，如果不存在则返回 404
            workorder = get_object_or_404(WorkOrder, id=workorder_id)
            # 从请求体中解析 JSON 数据
            data = json.loads(request.body)
            # 更新工单的字段
            for key, value in data.items():
                setattr(workorder, key, value)
            # 保存更新后的工单
            workorder.save()
            return JsonResponse({'message': '工单更新成功'}, status=200)
        except Exception as e:
            # 返回错误信息
            return JsonResponse({'error': str(e)}, status=400)
    # 如果请求方法不是 PUT，返回 405 错误
    return JsonResponse({'error': '无效的请求方法'}, status=405)

# 删除工单
def delete_workorder(request, workorder_id):
    if request.method == 'DELETE':
        try:
            # 根据 ID 查询工单，如果不存在则返回 404
            workorder = get_object_or_404(WorkOrder, id=workorder_id)
            # 删除工单
            workorder.delete()
            return JsonResponse({'message': '工单删除成功'}, status=200)
        except Exception as e:
            # 返回错误信息
            return JsonResponse({'error': str(e)}, status=400)
    # 如果请求方法不是 DELETE，返回 405 错误
    return JsonResponse({'error': '无效的请求方法'}, status=405)