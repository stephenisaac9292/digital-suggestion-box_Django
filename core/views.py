
from .models import Suggestion
from .serializers import SuggestionSerializer
from .permissions import IsOwnerOrReadOnly
from .serializers import SignupSerializer
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken



class SuggestionViewSet(viewsets.ModelViewSet):
    queryset = Suggestion.objects.all().order_by('-created_at')
    serializer_class = SuggestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)





class SignupView(generics.CreateAPIView):  # ✅ Only one class definition here
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # 🧪 DEBUG: Wrap token generation in try/except
        try:
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)

            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': access,
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print("❌ Error during token generation:", str(e))  # Terminal output
            return Response({
                "detail": f"Token generation failed: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)