from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        """
        Handle user registration and return user data along with authentication token.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user, token = serializer.save()
            return Response({
                "user": serializer.data,
                "token": token.key,
                "message": "User created successfully"
            }, status=201)
        return Response(serializer.errors, status=400)

class LoginUserView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key
            })
        return Response({"detail": "Invalid credentials"}, status=400)
