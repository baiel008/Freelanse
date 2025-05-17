from rest_framework import serializers
from .models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'skill_name']


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'role']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role',
                  'bio', 'avatar', 'skills', 'social_links', 'date_registered']



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']



class ProjectListSerializer(serializers.ModelSerializer):
    client = UserProfileListSerializer()
    deadline = serializers.DateField(format='%d-%m-%Y')
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Project
        fields = ['id', 'title', 'budget', 'status', 'deadline', 'created_at', 'client']


class ProjectDetailSerializer(serializers.ModelSerializer):
    client = UserProfileListSerializer()
    category = CategoryListSerializer()
    skills_required = SkillSerializer(many=True)
    deadline = serializers.DateField(format='%d-%m-%Y')
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'budget', 'deadline', 'status',
            'category', 'skills_required', 'client', 'created_at'
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_projects = ProjectListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_projects']



class OfferSerializer(serializers.ModelSerializer):
    freelancer = UserProfileListSerializer()
    project = ProjectListSerializer()
    proposed_deadline = serializers.DateField(format='%d-%m-%Y')
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Offer
        fields = [
            'id', 'project', 'freelancer', 'message',
            'proposed_budget', 'proposed_deadline', 'created_at'
        ]



class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserProfileListSerializer()
    target = UserProfileListSerializer()
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Review
        fields = ['id', 'project', 'reviewer', 'target', 'rating', 'comment', 'created_at']
