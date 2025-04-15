from django.urls import path
from workorder import views

urlpatterns = [

    # create
    path('create/', views.create_workorder, name='create_workorder'),  # 增
    # delete
    path('delete/<int:workorder_id>/', views.delete_workorder, name='delete_workorder'),  # 删



    
]