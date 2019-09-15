from django.urls import path
from .views import PostListView, PostDetailView
from django.conf.urls.static import static

from django.conf import settings

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='lista'),
    path('<str:slug>', PostDetailView.as_view(), name='detalhe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
