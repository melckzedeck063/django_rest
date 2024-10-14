from itertools import count
from smtpd import program

from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_app import serializer
from rest_app.models import Student, Program
from rest_app.serializer import StudentSerializer, ProgramSerializer


# Create your views here.

@api_view(["POST"])
def create_update_student(request):
    data =  request.data
    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
        try:
            program = Program.objects.get(id=data.get("program"))
            # serializer.save()
            student_instance = serializer.save(program=program)
            return Response({"error" : False,"data":StudentSerializer(student_instance).data, "message": "Student created successfully"},200)
        except Program.DoesNotExist:
            return Response({"error": True, "message": "Program not found"}, status=400)
    return Response(serializer.errors)


@api_view(["GET"])
def get_student(request):
    queryset = Student.objects.all()
    serializer =  StudentSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_student_by_id(request, id):
    queryset = Student.objects.filter(id=id).first()
    serializer =  StudentSerializer(queryset,many=False)
    return Response(serializer.data)

@api_view(["GET"])
def get_student_by_program(request, id):
    queryset = Student.objects.filter(program__id=id)
    serializer =  StudentSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_program(request):
    data = request.data
    serializer =  ProgramSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "error": False,
            "data": serializer.data,
            "message": "Program created successfully"
        }, status=200)
    return Response(serializer.errors)



@api_view(["GET"])
def get_programs(request):
    queryset = Program.objects.all()
    serializer =  ProgramSerializer(queryset,many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_program(request,id):
    try:
        queryset =  Program.objects.get(id=id)
        queryset.delete()
        return Response({"error" : False, "data": {}, "message" : "Deleted program successfully"}, status=200)
    except Program.DoesNotExist:
        return Response({"error":"Program not found"}, status=404)