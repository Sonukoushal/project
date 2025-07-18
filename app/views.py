from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer

class StudentGet(APIView):
    def get(self,request):
        object=Student.objects.all()
        serializer=StudentSerializer(object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class StudentGetOne(APIView):
    def get(self,request,id):
        try:
            object=Student.objects.get(id=id)
            serializer=StudentSerializer(object)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"error":"object not found"},status=status.HTTP_404_NOT_FOUND)
        
class StudentAdd(APIView):
    def post(self,request):
        try:
            serializer=StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class StudentUpdate(APIView):
    def put(self,request,id):
        try:
            object=Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"error":"object not found"},status=status.HTTP_404_NOT_FOUND)
        serializer=StudentSerializer(object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class StudentPatch(APIView):
    def patch(self,request,id):
        try:
            object=Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"error":"object not found"},status=status.HTTP_404_NOT_FOUND)
        serializer=StudentSerializer(object,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class StudentDelete(APIView):
        def delete(self,request,id):
            try:
                object=Student.objects.get(id=id)
                object.delete()
                return Response({"success":"student delete"},status=status.HTTP_204_NO_CONTENT)
            except Student.DoesNotExist:
                return Response({"error":"Object not found"},status=status.HTTP_404_NOT_FOUND)
            
            



        

