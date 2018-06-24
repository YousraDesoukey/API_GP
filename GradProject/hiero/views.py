# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Image
import subprocess
from rest_framework.response import Response
from django.http import Http404,HttpResponse
from rest_framework import status
#from .serializers import ImageSerializer
import base64,os
from rest_framework.parsers import MultiPartParser



class ImageView(APIView):
    def post(self, request,format=None):
            imgdata = base64.b64decode(request.data['data'])
            with open('filename.jpg', 'wb') as f:
                f.write(imgdata)        
            #return Response('done')

            cmd = [ 'python', 'DL.py']
            output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
            print (output)
            return Response(output)

def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)



