from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
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
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Call the parent class to handle the normal token behavior
        response = super().post(request, *args, **kwargs)

        # Add custom fields or behavior to the response if necessary
        # For example, return user data along with the token
        if response.status_code == status.HTTP_200_OK:
            user = request.user
            response.data['username'] = user.username
            response.data['email'] = user.email

        return response
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
