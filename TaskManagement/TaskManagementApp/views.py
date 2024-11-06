from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from .models import Task


class UserRegistration(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        UserModel = get_user_model()
        if not email:
            return Response({"Error":"Please provide email"},status=status.HTTP_400_BAD_REQUEST)
        if UserModel.objects.filter(email=email).exists():
            return Response({"Error":"Email already exists"},status=status.HTTP_409_CONFLICT)
        if not password:
            return Response({"Error":"Please provide password"},status=status.HTTP_400_BAD_REQUEST)
        try:
            UserModel.objects.create_user(email=email,password=password)
        except:
            return Response({"Error":"Exception ocurred while creating user"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"success":"User Successfully Created"},status=status.HTTP_201_CREATED)
    


class Tasks(APIView):

    def post(self, request):
        data = request.data
        if not data.get("title"):
            return Response({"Error":"Please provide title"},status=status.HTTP_400_BAD_REQUEST)
        if not data.get("status"):
            return Response({"Error":"Please provide status"},status=status.HTTP_400_BAD_REQUEST)
        task_obj = Task.objects.create(title = data.get("title"), description=data.get("description"),
                            status=data.get("status"))
        task_obj.user_id = request.user
        task_obj.save()
        return Response({"success":"task has been created successfully"},status=status.HTTP_201_CREATED)
    
    def get(self, request):
        all_tasks = Task.objects.values()
        return Response(all_tasks,status=status.HTTP_200_OK)
    
class TaskDetails(APIView):

    def get(self, request, task_id):
        if Task.objects.filter(id=task_id).exists():
            task_obj = Task.objects.get(id=task_id)
            return Response({"title":task_obj.title,"description":task_obj.description,"status":task_obj.status},status=status.HTTP_200_OK)
        return Response({"Error":"Task does not exists"},status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, task_id):
        data = request.data
        if Task.objects.filter(id=task_id).exists():
            task_obj = Task.objects.get(id=task_id)
            task_obj.title = data.get("title")
            task_obj.description = data.get("description")
            task_obj.status = data.get("status")
            return Response({"title":task_obj.title,"description":task_obj.description,"status":task_obj.status})
        return Response({"Error":"Task does not exists"},status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, task_id):
        if Task.objects.filter(id=task_id).exists():
            Task.objects.filter(id=task_id).delete()
            return Response({"Success":"Task deleted successully"},status=status.HTTP_200_OK)
        return Response({"Error":"Task does not exists"},status=status.HTTP_404_NOT_FOUND)



