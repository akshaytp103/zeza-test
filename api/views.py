from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
import pandas as pd
from rest_framework.parsers import FileUploadParser
from .models import CSVData
from .serializers import CSVDataSerializer
import codecs
import csv

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action



fs = FileSystemStorage(location='file')


class CSVDataViewSet(viewsets.ModelViewSet):
    queryset = CSVData.objects.all()
    serializer_class = CSVDataSerializer
    # parser_classes = (FileUploadParser,)
    
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        """Upload data from CSV"""
        file = request.FILES["file"]

        content = file.read()  # these are bytes
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)
        
        CSVData_list = []
        for id_, row in enumerate(reader):
            (
                
                name,
                email,
                location,
                
            ) = row
            CSVData_list.append(
                CSVData(
                    
                    name=name,
                    email=email,
                    location=location,
                )
            )

        CSVData.objects.bulk_create(CSVData_list)

        return Response("Successfully upload the data")
    
#     def post(self, request, *args, **kwargs):
#         serializer_class = self.serializer_class(data=request.data)

#         if serializer_class.is_valid():
#             file = serializer_class.validated_data['file']

#             df = pd.read_csv(file)

#             # Store the data in the database
#             for index, row in df.iterrows():
                
#                 CSVData.objects.create(
#                     name=row['name'],
#                     email=row['email'],
#                     location=row['location'],
#                 )
                
#             return Response(serializer_class.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

# def create_db(file_path):
#     df_u=pd.read_csv(file_path,delimiter=',')
#     list_of_csv = [list(row) for row in df_u.values]
    
#     for l in list_of_csv:
#         CSVData.objects.create(
#             name=1[1],
#             email=1[2],
#             location=1[3],
#         )
        
# def main(request):
    
#     if request.method=="POST":
#         file =request.FILES['file']
#         obj = file.objects.create(file=file)
#         create_db(obj.file)
#     return render(request,'main.html')