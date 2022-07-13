from rest_framework import serializers

from .models import StudentModel,TransactionModel

class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = StudentModel
        fields = ('unid',
        'name',
        'phone',
        'gender',
        'father',
        'mother',
        'address',
        'group',
        'age',
        'dob',
        'speechTherapy',
        'therapy',
        'transportation',
        'admissionCharge',
        'monthlyCharge',
        'snacks')

class TransactionSerializers(serializers.ModelSerializer):

    class Meta:
        model = TransactionModel
        fields=(
            'studentunid',
            'date',
            'paidAmount',
            'forMonth',
            'speechTherapy',
            'therapy',
            'transportation',
            'admissionCharge',
            'monthlyCharge',
            'snacks',
            'paid'
        )