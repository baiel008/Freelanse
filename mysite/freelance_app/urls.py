from .views import *
from django.urls import path, include
from rest_framework import routers



router =routers.SimpleRouter()
router.register(r'skill', SkillViewSet, basename='skill_list')
router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'offer', OfferViewSet, basename='offer_list')
router.register(r'review', ReviewViewSet, basename='review_list')


urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('project/', ProjectListAPIView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailAPIView.as_view(), name='project_detail'),
]