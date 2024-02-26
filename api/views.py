from rest_framework.authtoken.models import Token
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnlySample, IsOwnerOrReadOnlyResult, IsOwnerOrReadOnlySubject
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, ProfileSerializer, SampleSerializer, ResultSerializer, SubjectSerializer
from django.contrib.auth.models import User
from users.models import Profile
from analysis.models import Result, Subject, Sample


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.forms import UserSignupForm

from django.contrib.auth.forms import AuthenticationForm


class LoginAPIView(APIView):
    def post(self, request):
        form = AuthenticationForm(data=request.data)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = form.get_user()
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)


class SignUpAPIView(APIView):
    def post(self,request):
        form = UserSignupForm(request.data)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=True
            user.save()

            return Response({'detail':'user registerd successful'},status=status.HTTP_201_CREATED)
        else:
             return Response({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
        


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAdminUser,)


class SampleView(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnlySample,)

    def get_queryset(self):
        user = self.request.user 
        return self.queryset.filter(subject__user=user)
    
    # def get_object(self):
    #     sample = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
    #     self.check_object_permissions(self.request, sample)
    #     return sample

    def create(self, request, *args, **kwargs):
        subject = Subject.objects.filter(user=request.user).first()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(subject=subject)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ResultView(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnlyResult,)

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(sample__subject__user=user)

    def get_object(self):
        result = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, result)
        return result

class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnlySubject,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user 
        return self.queryset.filter(user=user)
    
    def get_object(self):
        subject = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, subject)
        return subject