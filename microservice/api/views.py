from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer
import requests

class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()

            email_data = {
                "email_to": serializer.validated_data['email'],
                "subject": "Welcome to YourApp",
                "template": "registration_email_template",
                "template_data": {"username": serializer.validated_data['username']}
            }

            response = requests.post('http://localhost:8000/send-email', json=email_data)
            response.raise_for_status()
            
            return Response({"status_code": 200, "data": "User registered and email sent successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Handle any exceptions, log them, and return an appropriate response
            return Response({"status_code": 500, "data": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
