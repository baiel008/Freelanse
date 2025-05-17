from rest_framework import serializers
from .models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']



class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Project
        fields = ['id', 'created_at', 'deadline']


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_project = ProjectListSerializer()
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_project']


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'