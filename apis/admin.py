from django.contrib import admin
from .models import StudentModel,TransactionModel
# Register your models here.

admin.site.register(StudentModel)
admin.site.register( TransactionModel)