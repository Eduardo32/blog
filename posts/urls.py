from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.conf.urls.static import static

from django.conf import settings

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='lista'),
    path('novo/', PostCreateView.as_view(), name='novo'),
    path('<str:slug>/', PostDetailView.as_view(), name='detalhe'),
    path('edita/<str:slug>/', PostUpdateView.as_view(), name='edita'),
    path('exclui/<str:slug>', PostDeleteView.as_view(), name='exclui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
