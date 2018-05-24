from django.shortcuts import render, HttpResponse
from mimetypes import MimeTypes
import os
import json
import requests


def index(request):
    cl_platform = str(request.user_agent.os.family)
    cl_ver = str(request.user_agent.os.version_string)
    query_s = cl_platform + ' ' + cl_ver

    query = {'query': query_s,
             'references': True,
             'sort': 'published',
             'fields': ['id', 'title', 'type', 'bulletinFamily', 'published', 'modified', 'href'],
             }
    headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
    res = requests.post('https://vulners.com/api/v3/search/lucene', data=json.dumps(query), headers=headers)
    print(type(res.text))
    file_name = 'file.txt'
    with open(file_name, 'w') as f:
        json.dump(res.json(), f, indent=3)

    return render(request, 'index.html', {'query': query_s, 'output': res.text})


def save_file(request):
    file_name = 'file.txt'
    mime = MimeTypes()
    with open(file_name, 'rb') as f:
        response = HttpResponse(f.read())

        file_type = mime.guess_type(file_name)
        if file_type is None:
            file_type = 'application/octet-stream'

        response['Content-Type'] = file_type
        response['Content-Length'] = str(os.stat(file_name).st_size)
        response['Content-Disposition'] = "attachment; filename=" + file_name

        return response
