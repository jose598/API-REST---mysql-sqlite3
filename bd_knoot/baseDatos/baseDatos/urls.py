from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from Knoot_db.views import AnuncioViewSet

router = DefaultRouter()
router.register(r'anuncios',AnuncioViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
