from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from django.contrib.auth import get_user_model  # Import to get the custom user model

CustomUser = get_user_model()  # Reference to custom user model

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
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

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access this view

    def post(self, request, user_id):
        # Get the user to follow
        user_to_follow = CustomUser.objects.filter(id=user_id).first()
        if not user_to_follow:
            raise NotFound("User not found")

        user = request.user
        if user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Add the follow
        user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access this view

    def post(self, request, user_id):
        # Get the user to unfollow
        user_to_unfollow = CustomUser.objects.filter(id=user_id).first()
        if not user_to_unfollow:
            raise NotFound("User not found")

        user = request.user
        if user == user_to_unfollow:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the follow
        user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK
