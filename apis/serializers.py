from rest_framework import serializers

from .models import StudentModel

class StudentSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StudentModel
        fields = ('title','description')