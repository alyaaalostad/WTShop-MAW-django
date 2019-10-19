
from django.contrib import admin
from django.urls import path

from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('items/', views.ItemsList.as_view(), name="items-list"),

    path("checkout/", views.CheckoutCart.as_view(), name="chekout"),
    path('profile/', views.UserProfile.as_view(), name='user-profile'),

    path("register/", views.Register.as_view(), name="register"),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),   	
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
