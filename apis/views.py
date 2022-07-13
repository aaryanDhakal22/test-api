from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from apis.models import StudentModel
from apis.serializers import StudentSerializers

from apis.models import TransactionModel
from apis.serializers import TransactionSerializers

from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        students = StudentModel.objects.all()

        name = request.GET.get('name',None)
        print(name)
        if name is not None:
            students = students.filter(name__icontains=name)
        student_serializer = StudentSerializers(students,many=True)
        return JsonResponse(student_serializer.data,safe=False)


    elif request.method == "POST":
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializers(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def student_detail(request,unid):
    try:
        student = StudentModel.objects.get(pk=unid)
    except StudentModel.DoesNotExist :
        return JsonResponse({'message':"The student does not exist"},status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        student_serializer = StudentSerializers(student)
        return JsonResponse(student_serializer.data)
    elif request.method == "PUT":
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializers(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data)
        return JsonResponse(student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message':'Student data was deleted successfully'},status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
def transaction_list(request,unid):
    if request.method == 'GET':
        transactions = TransactionModel.objects.all()

        unid = request.GET.get('unid',None)
        if unid is not None:
            transactions = transactions.filter(unid__icontains=unid)
        transaction_serializer = TransactionSerializers(transactions,many=True)
        return JsonResponse(transaction_serializer.data,safe=False)


    elif request.method == "POST":
        transaction_data = JSONParser().parse(request)
        transaction_serializer = TransactionSerializers(data=transaction_data)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            return JsonResponse(transaction_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(transaction_serializer.errors,status=status.HTTP_400_BAD_REQUEST)