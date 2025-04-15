from django.db import models

class WorkOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', '待处理'),
        ('in_progress', '处理中'),
        ('completed', '已完成'),
    ]

    name = models.CharField(max_length=255, verbose_name="名称")
    time = models.DateTimeField(verbose_name="时间")
    location = models.CharField(max_length=255, verbose_name="地点")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="状态"
    )
    details = models.TextField(verbose_name="具体内容")
    supplies_needed = models.TextField(verbose_name="所需用品", blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="预算")
    assigned_engineer_id = models.IntegerField(verbose_name="被指派的工程师ID")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "工单"
        verbose_name_plural = "工单"