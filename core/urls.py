from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuggestionViewSet, SignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'suggestions', SuggestionViewSet, basename='suggestion')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
