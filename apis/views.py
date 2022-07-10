from rest_framework import viewsets

from .serializers import StudentSerializers
from .models import StudentModel

class StudentViewSet(viewsets.ModelViewSet):

    queryset = StudentModel.objects.all()

    serializer_class = StudentSerializers