
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('items/', views.ItemsList.as_view(), name="items-list"),
    path('items/<int:item_id>/', views.ItemDetail.as_view(), name="item-detail"),

    path("register/", views.Register.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name='login'),
   	
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
