from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group

# Create your models here.
class RealStockAccountCashTransfer(models.Model):
    account = models.CharField(max_length=20,default = '011C263979',verbose_name = 'Tài khoản' )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Ngày tạo' )
    modified_at = models.DateTimeField(auto_now=True, verbose_name = 'Ngày chỉnh sửa' )
    date = models.DateField( default=timezone.now,verbose_name = 'Ngày nộp tiền' )
    amount = models.FloatField(verbose_name = 'Số tiền')
    description = models.TextField(max_length=255, blank=True,verbose_name = 'Mô tả')
    user_created = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank= True,                   verbose_name="Người tạo")
    user_modified = models.CharField(max_length=150, blank=True, null=True,
                             verbose_name="Người chỉnh sửa")
    class Meta:
         verbose_name = 'Sao kê tiền TKCK'
         verbose_name_plural = 'Sao kê tiền TKCK'
    
    def __str__(self):
        return str(self.amount) 
    
class RealBankCashTransfer(models.Model):
    account = models.CharField(max_length=20,default = 'TCB',verbose_name = 'Tài khoản' )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Ngày tạo' )
    modified_at = models.DateTimeField(auto_now=True, verbose_name = 'Ngày chỉnh sửa' )
    date = models.DateField( default=timezone.now,verbose_name = 'Ngày nộp tiền' )
    amount = models.FloatField(verbose_name = 'Số tiền')
    description = models.TextField(max_length=255, blank=True,verbose_name = 'Mô tả')
    user_created = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank= True,                   verbose_name="Người tạo")
    user_modified = models.CharField(max_length=150, blank=True, null=True,
                             verbose_name="Người chỉnh sửa")
    class Meta:
         verbose_name = 'Sao kê tiền TKNH'
         verbose_name_plural =  'Sao kê tiền TKNH'
    
    def __str__(self):
        return str(self.amount) 
    
class RealTradingPower(models.Model):
    account = models.CharField(max_length=20,default = '011C263979',verbose_name = 'Tài khoản' )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Ngày tạo' )
    modified_at = models.DateTimeField(auto_now=True, verbose_name = 'Ngày chỉnh sửa' )
    date = models.DateField( default=timezone.now,verbose_name = 'Ngày' )
    max_amount = models.FloatField(verbose_name = 'Sức mua tối đa')
    min_amount = models.FloatField(verbose_name = 'Sức mua tối thiểu')
    description = models.TextField(max_length=255, blank=True,verbose_name = 'Mô tả')
    user_created = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank= True,                   verbose_name="Người tạo")
    user_modified = models.CharField(max_length=150, blank=True, null=True,
                             verbose_name="Người chỉnh sửa")
    class Meta:
         verbose_name = 'Sức mua tài khoản'
         verbose_name_plural = 'Sức mua tài khoản'
    
    def __str__(self):
        return str(self.date) 