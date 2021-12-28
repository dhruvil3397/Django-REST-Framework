from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
import requests
from django.http.response import JsonResponse
from requests.api import request
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer,TokenSerializer,UserProfileSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login
from .models import UserProfile
import random
import string
from .decorators import user_is_entry_author
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
import pyotp
from django.core.exceptions import ObjectDoesNotExist
import base64

# Sending an email with the data
import smtplib
from email.message import EmailMessage
import time

# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def userdetails(request,pk=None):
    if request.method == 'GET':
        if pk is not None:
            stu = User.objects.get(id=pk)
            serializer = UserSerializer(stu)
            return Response(serializer.data)
        stu = User.objects.all()
        serializer = UserSerializer(stu,many= True)
        print(serializer.data)
        
        return Response(serializer.data)
    
    if request.method =='POST':
        # request.body gives json data
        # request.data gives python data

        email = request.data.get('email')
        # split the email from '@' to get username
        b = email.split('@') # it provides the list of split data
        print(b[0])
        username = b[0]

        # For Auto Password Generation :----------
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        all = lower + upper + num + symbols
        temp = random.sample(all,12)
        password = "".join(temp)
        print(password)
        print('--------------')

        # User.objects.create_user(username,email,password) This creates new user
        user = User.objects.create_user(username,email,password)
        user.save()

        # Save the values in UserProfile model:-----------------
        userprofile = UserProfile()
        userprofile.user = user
        userprofile.permission = "Uploader" # This select only Uploader permission
        userprofile.save()

        # Here, Token Generations :-------------------------
        token_create = Token.objects.get_or_create(user = user)
        # Get the particular user's Token
        token = Token.objects.get(user=user)
        stu = TokenSerializer(token) # serialize the token-complex to python
        token_key = stu.data['key'] # It provides token_key

        # SMTP email sending :--------------------------------
        msg =  EmailMessage()
        msg['Subject'] = 'Welcome'
        msg['From'] = 'sonidhruvil708@gmail.com'
        msg['To'] = email
        msg.set_content(f'Your Login Credential is Username: {username}  Password :{password}  Token:{token_key}')

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server :
            server.login("","") #  Enter email_id and password
            server.send_message(msg)

        print("Email Sent!!!")
        # Send the data in Json format
        data = {'username':username,'email':email,'permission':userprofile.permission,'token':token_key}
        
        return Response(data,status = status.HTTP_201_CREATED)

# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(email):
        return 'JBSWY3DPEHPK3PXP'+str(email)

@api_view(['GET','POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)
        print(password)
        b = email.split('@')
        username = b[0] 
        print(username) 
        
        # Here, Authenticate the username and password using django Authentication
        user1 = authenticate(username=username,password=password) 
        # If user1 is not authenticated,then returns None value,so we get Invalid credential response
        # If user1 is validated, it returns the user
        if user1 is not None :
            print(user1.email)
            if  email ==user1.email:
                keygen = generateKey()
                key = base64.b32encode(keygen.returnValue(user1.email).encode())  # Key is generated
                print(key)
                # interval = 300 means after 300 seconds, otp will expire
                totp = pyotp.TOTP(key,interval =300)  # TOTP Model for OTP is created
                otp = totp.now()
                print(otp)

                token = Token.objects.get(user=user1)
                stu = TokenSerializer(token)
                token_key = stu.data['key']

                 # SMTP email sending :--------------------------------
                msg =  EmailMessage()
                msg['Subject'] = 'Welcome'
                msg['From'] = 'sonidhruvil708@gmail.com'
                msg['To'] = 'ds@yopmail.com'
                msg.set_content(f'Your OTP is :{otp}')

                with smtplib.SMTP_SSL('smtp.gmail.com',465) as server :
                    server.login("","")
                    server.send_message(msg)
                print("Email Sent!!!")

                data = {'token':token_key}
                return Response(data)
            else :
                emsg = {'msg': 'Invalid credentials,please enter valid email or password'}
                return Response(emsg)
        else:
            emsg = {'msg': 'Invalid credentials,please enter valid email or password'}
            return Response(emsg)
# OTP Verification :-------------------------

@api_view(['GET','POST'])
def otpverify(request,email):
    if request.method == 'POST':
        try :
            user = User.objects.get(email=email)
            otp = request.data.get('otp')
            print(otp)
            keygen = generateKey()
            key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
            print(key)
            totp = pyotp.TOTP(key,interval=300)
            verify = totp.verify(otp)
            print(verify)
            if verify == True:
                return Response({'msg':'OTP is successfully verified'})
            return Response({'msg':'OTP is invalid'})
        except:
            return Response({'msg':'OTP is invalid'})



@csrf_exempt
@user_is_entry_author('Admin','Uploader','Editor')
@api_view(['GET','POST','PUT'])
def edit(request):
    if request.method =='PUT':
        firstname = request.data.get('firstname')
        lastname = request.data.get('lastname')
        birtdate = request.data.get('birthdate')
        phone = request.data.get('phone')
        image = request.data.get('image')
        print('*************')
        print(image)
        print(firstname)
        print(lastname)
        print('************')
        
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        print(token)
        user_id = Token.objects.get(key=token).user_id
        print(user_id)
        user = User.objects.get(id=user_id)
        print(user)
        print('***********')
        stu = UserProfile.objects.get(user =user)
        
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        stu.birthdate = birtdate
        stu.phone = phone
        stu.image = image
        stu.save()
        data = {'msg':'Data Updated'}
        return Response(data)
    return Response({'msg':'Error'})

# Change Password :------------------------------------
@csrf_exempt
@user_is_entry_author('Admin','Uploader','Editor')
@api_view(['PUT'])
def changepassword(request):
    if request.method == 'PUT':
        email = request.data.get('email')
        old_pass = request.data.get('old_pass')
        new_pass = request.data.get('new_pass')
        user = User.objects.get(email=email)
        print(user.password)
        # here I use string format , so covert old_pass and new_pass in string format
        if user.check_password('{}'.format(old_pass)) == True:
            user.set_password('{}'.format(new_pass))
            print(user.set_password)
            user.save()
            # SMTP email sending :--------------------------------
            msg =  EmailMessage()
            msg['Subject'] = 'Welcome'
            msg['From'] = 'dhruvillr33@gmail.com'
            msg['To'] = 'ds@yopmail.com'
            msg.set_content(f'Your New Login Credential is Username: {user.username}  Password :{new_pass}')

            with smtplib.SMTP_SSL('smtp.gmail.com',465) as server :
                server.login("","")
                server.send_message(msg)
            print("Email Sent!!!")

            data = {'username':user.username,'new_password':new_pass}
            return Response(data)
        else  :
            return JsonResponse({'msg':'Your old_password is invalid'})               


# Reset Password :--------------------------------
@csrf_exempt
@user_is_entry_author('Admin')
@api_view(['PUT'])
def resetpassword(request):
    if request.method == 'PUT':
        id = request.data.get('id')
        new_pass = request.data.get('new_pass')
        user = User.objects.get(id=id)
        print(type(id))
        print(user.password)
    
        print(type(str(user.id)))
        # here I use string format , so covert old_pass and new_pass in string format
        if str(user.id) == id:
            user.set_password('{}'.format(new_pass))
            print(user.set_password)
            user.save()
            # SMTP email sending :--------------------------------
            msg =  EmailMessage()
            msg['Subject'] = 'Welcome'
            msg['From'] = 'sonidhruvil708@gmail.com'
            msg['To'] = 'ds@yopmail.com'
            msg.set_content(f'The reset password is : {new_pass} for this user :{user.username} and this email :{user.email}')

            with smtplib.SMTP_SSL('smtp.gmail.com',465) as server :
                server.login("","")
                server.send_message(msg)
            print("Email Sent!!!")

            data = {'username':user.username,'new_password':new_pass}
            return Response(data)
        else :
            return JsonResponse({'msg':'User id does not exist'})
       

# Forgot Password :----------------------------------
@csrf_exempt
@user_is_entry_author('Admin','Uploader','Editor')
@api_view(['POST'])
def forgotpassword(request):
    if request.method == 'POST':
        email = request.data.get('email')
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
        print(key)
        # interval = 300 means after 300 seconds, otp will expire
        totp = pyotp.TOTP(key,interval =300)  # TOTP Model for OTP is created
        otp = totp.now()
        print(otp)
     
        # SMTP email sending :--------------------------------
        msg =  EmailMessage()
        msg['Subject'] = 'Welcome'
        msg['From'] = 'sonidhruvil708@gmail.com'
        msg['To'] = 'ds@yopmail.com'
        msg.set_content(f'Your OTP is :{otp}')

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server :
            server.login("","")
            server.send_message(msg)
        print("Email Sent!!!")

        data = {'otp':otp}
        return Response(data)
        
# Verify the forgot password:------------------------------
@csrf_exempt
@user_is_entry_author('Admin','Uploader','Editor')
@api_view(['POST'])  
def verifyforgotpass(request):
    if request.method =='POST':
        otp = request.data.get('otp')
        email = request.data.get('email')
        new_pass = request.data.get('new_pass')
        try :
            user = User.objects.get(email=email)
            otp = request.data.get('otp')
            print(otp)
            keygen = generateKey()
            key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
            print(key)
            totp = pyotp.TOTP(key,interval=300)
            verify = totp.verify(otp)
            print(verify)
            if verify == True:
                user = User.objects.get(email=email)
                user.set_password('{}'.format(new_pass))
                print(user.set_password)
                user.save()
                # SMTP email sending :--------------------------------
                msg =  EmailMessage()
                msg['Subject'] = 'Welcome'
                msg['From'] = 'sonidhruvil708@gmail.com'
                msg['To'] = 'ds@yopmail.com'
                msg.set_content(f'Your New password is :{new_pass}')

                with smtplib.SMTP_SSL('smtp.gmail.com',465) as server :
                    server.login("","")
                    server.send_message(msg)
                print("Email Sent!!!")
                return Response({'msg':'Your new password is successfully created!!!'})
            return Response({'msg':'OTP is invalid'})
        except:
            return Response({'msg':'OTP is invalid'})

# # # Admin Read list of users data,update user's data and delete user's data
# @csrf_exempt
# @user_is_entry_author('Admin')
# @api_view(['GET','PUT','DELETE'])  
# def adminRUD(request):
#     if request.method == 'GET':
#         id = request.data.get('id',None)
#         if id is not None:
#             stu = User.objects.get(id=id)
#             serializer = UserSerializer(stu)
#             return Response(serializer.data)
#         stu = User.objects.all()
       
#         # profile = UserProfile.objects.all().defer('image')

#         # pro_serializer = UserProfileSerializer(profile,many=True)
       
#         serializer = UserSerializer(stu,many= True)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         id = request.data.get('id',None)
#         firstname = request.data.get('firstname')
#         lastname = request.data.get('lastname')
#         birtdate = request.data.get('birthdate')
#         phone = request.data.get('phone')
#         image = request.data.get('image')
#         if id is not None:
#             user = User.objects.get(id = id)
#             stu = UserProfile.objects.get(user =user)
#             user.first_name = firstname
#             user.last_name = lastname
#             print(user.last_name)
#             user.save()
#             stu.birthdate = birtdate
#             stu.phone = phone
#             stu.image = image
#             stu.save()
#             data = {'msg':'Data Updated'}
#             return Response(data)
#         return Response({'msg':'The user id does not exist'})

#       # Delete the data
#     if request.method == 'DELETE':
#         id = request.data.get('id',None)
#         if id is not None:
#             user = User.objects.get(id = id)
#             user.delete()
            
#             data = {'msg':'Data Deleted'}
#             return Response(data)
#         else :
#             return JsonResponse({'msg':'The user id does not exist'})
        
# OR  In this function,we update the data using serializer class:----------------------------------
# Admin Read list of users data,update user's data and delete user's data
@csrf_exempt
@user_is_entry_author('Admin')
@api_view(['GET','PUT','DELETE'])  
def adminRUD(request):
    if request.method == 'GET':
        id = request.data.get('id',None)
        if id is not None:
            stu = User.objects.get(id=id)
            serializer = UserSerializer(stu)
            return Response(serializer.data)
        stu = User.objects.all()
       
        # profile = UserProfile.objects.all().defer('image')

        # pro_serializer = UserProfileSerializer(profile,many=True)
       
        serializer = UserSerializer(stu,many= True)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        id = request.data.get('id',None)
        print('**********')
        if id is not None:
            user_obj = User.objects.get(id=id)
            print(user_obj)
            user_serializer = UserSerializer(user_obj,data = request.data)

            profile_obj = UserProfile.objects.get(user_id=id)
            profile_serializer = UserProfileSerializer(profile_obj,data=request.data)
            

            if user_serializer.is_valid() and profile_serializer.is_valid():
                user_serializer.save()
                profile_serializer.save()

                data = {'msg':'Data Updated'}
                return Response(data)
            return Response(profile_serializer.errors)
        return Response({'msg':'The user id does not exist'})

      # Delete the data
    if request.method == 'DELETE':
        id = request.data.get('id',None)
        if id is not None:
            user = User.objects.get(id = id)
            user.delete()
            
            data = {'msg':'Data Deleted'}
            return Response(data)
        else :
            return JsonResponse({'msg':'The user id does not exist'})


        
        

       

        
        
        

       
            


