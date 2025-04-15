from django.urls import path
# 导入view
from engineer import views

urlpatterns = [
    #add_engineer
    path('add/', views.add_engineer, name='add_engineer'),  # 增
    #delete_engineer
    path('delete/<int:engineer_id>/', views.delete_engineer, name='delete_engineer'),  # 删
    #get_engineer
    path('get/<int:engineer_id>/', views.get_engineer, name='get_engineer'),  # 查
    #update_engineer
    path('update/<int:engineer_id>/', views.update_engineer, name='update_engineer'),  # 改
    #getall
    path('getall/', views.get_all_engineers, name='get_all_engineers'),  # 查所有
    #demo
    path('demo/', views.demo, name='demo'),  # demo

]