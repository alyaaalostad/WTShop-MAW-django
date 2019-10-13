
from django.contrib import admin
from django.urls import path

from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('items/', views.ItemsList.as_view(), name="items-list"),
    path('item/<int:item_id>/', views.ItemDetail.as_view(), name="item-detail"),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
