from rest_framework.decorators import api_view
from . models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@api_view (['GET'])
def student_details(request):
    students= Students.objects.all()
    serializer= StudentSerializer(students,many= True)
    return Response(serializer.data)

@api_view (['POST'])
def add_student_details(request):
    is_many = isinstance(request.data,list)
    serializer= StudentSerializer(data= request.data,many= is_many)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def update_student_details(request,student_id):
    student= get_object_or_404(Students,id=student_id)
    serializer= StudentSerializer(student,data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":f"Student {student_id} Updated Successfully"})
    return Response(serializer.errors)


@api_view(['DELETE'])
def delete_student_details(request,student_id):
    student = get_object_or_404(Students,id=student_id)
    student.delete()
    return Response({'message':f"The {student_id} is deleted successfully"})



