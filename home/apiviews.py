from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import *
from django.contrib.auth import authenticate, login, logout as log_out
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


class LoginAPI(APIView):

    def post(self, request):

        context={}
        context['message']='success'
        try:
            serializer = LoginSerializer(data=request.data)
            x =  serializer.is_valid()
        
            username = serializer.data['username']
            password = serializer.data['password']
                
            user_obj = authenticate(username=username, password=password)
            if not user_obj:
                return Response({'message':'No user exist'})

            login(request, user_obj)

            context['data']=serializer.data
            print('abcdef')


        except Exception as e:
            print(e)

        return  HttpResponseRedirect('/')
        
        return Response(context)



class RegisterAPI(APIView):

    def post(self, request):

        context={}
        context['messsage']='Unsuccess signup!, please fill valid data'
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']
                email = serializer.data['email']
                userobj, _ = User.objects.get_or_create(username=username,email=email)
                userobj.set_password(password)
                userobj.save()
                
                context['data']=serializer.data
                context['messsage']='success'


        except Exception as e:
            print(e)

        return Response(context)

@login_required
def logout(request):
    log_out(request)
    return  HttpResponseRedirect('/')
