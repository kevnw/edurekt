from rest_framework import generics

# Create your views here.
from lecturers.models import Lecturer
from lecturers.serializers import LecturerSerializer


class LecturerList(generics.ListCreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class LecturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer