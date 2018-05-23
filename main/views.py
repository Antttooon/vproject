from django.shortcuts import render, HttpResponse
# from django.http import  HttpResponse
from mimetypes import MimeTypes
import os
import platform
import json


# import vulners
import vulners







def index(request):
    vulners_api = vulners.Vulners()

    cl_platform =  str(request.user_agent.os.family)
    cl_ver = str(request.user_agent.os.version_string)
    query = cl_platform + ' '+ cl_ver

    res = vulners_api.search(query)

    file_name = 'file.txt'
    with open(file_name,'w') as f:
        json.dump(res,f, indent=8)
    return render(request, 'index.html',{'query':query,'res':json.dumps(res, indent=4)})




def save_file(request):
    file_name = 'file.txt'
    mime = MimeTypes()
    with open(file_name, 'rb') as f:
        response = HttpResponse(f.read())

        # file_type = mime.guess_type(file_name)
        # if file_type is None:
        #     file_type = 'application/octet-stream'

        response['Content-Type'] = 'application/json'
        response['Content-Length'] = str(os.stat(file_name).st_size)
        response['Content-Disposition'] = "attachment; filename="+file_name

        return response