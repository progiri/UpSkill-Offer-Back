from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import datetime, timedelta
from random import choice, sample
from string import digits, ascii_letters

from offers.settings import SECRET_KEY
from .models import *
from .serializers import *


class OfferAPI(APIView):
    def get(self, request):
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=http_status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)


class ResumeAPI(APIView):
    def get(self, request):
        resumes = Resume.objects.all()
        serializer = ResumeSerializer(resumes, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=http_status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)


class TokenAPI(APIView):
    prefix = ['jklT', '007D', 'SHA3']

    def checkToken(self, token):
        prefix_in_token = token[:4]
        salt = token[4: token.find('xl-')]
        finish_time = datetime.strptime(token[token.find('xl-') + len('xl-'): -4],'%Y-%m-%d %H:%M:%S')

        if salt != SECRET_KEY:
            return {'result': False, 'msg': 'fake token'}
        
        if prefix_in_token not in self.prefix:
            return {'result': False, 'msg': 'fake token'}

        if (datetime.now() - finish_time).days < 0:
            return {'result': False, 'msg': 'token expired'}
        
        return {'result': True, 'msg': 'norm token'}
     
    def createToken(self):
        salt = SECRET_KEY
        finish_time = datetime.now() + timedelta(hours=48)
        token = choice(self.prefix) + salt + 'xl-' + datetime.strftime(finish_time,'%Y-%m-%d %H:%M:%S') + ''.join(sample(ascii_letters + digits, 4))
        
        return token

    def post(self, request):
        data = request.data
        if data.get('do', 'no do') == 'check':
            check_result = self.checkToken(data.get('token', 'no token'))
            if check_result:
                return Response(data={'result': True}, status=http_status.HTTP_200_OK)
            else:
                return Response(data={'result': False, 'msg': check_result['msg']}, status=http_status.HTTP_400_BAD_REQUEST)

        elif data.get('do', 'no do') == 'create':
            if data.get('password', 'no password') == 'react+django':
                new_token = self.createToken()
                return Response(data={'result': True, 'token': new_token}, status=http_status.HTTP_200_OK)
            else:
                return Response(data={'result': False, 'msg': 'incorrect password'}, status=http_status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'result': False, 'msg': 'fuck off'}, status=http_status.HTTP_400_BAD_REQUEST)

        return Response(data={'token': 'abc123'}, status=http_status.HTTP_200_OK)