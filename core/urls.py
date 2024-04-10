from django.contrib import admin
from django.urls import re_path, path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
# from organizations.backends import invitation_backend

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('login/', views.LoginView.as_view(), name='login'),
    re_path('login-new/', views.UserDirectRegistrationView.as_view(), name='login-new'),
    re_path('signup/', views.SignupView.as_view(), name='signup'),
    re_path('test_token/', views.TestTokenView.as_view(), name='test_token'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
#     path(r'^accounts/', views('organizations.urls')),
#     path(r'^invitations/', views(invitation_backend().get_urls())),
]
