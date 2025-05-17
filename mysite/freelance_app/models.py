from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class Skill(models.Model):
    skill_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.skill_name


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='client')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    skills = models.ManyToManyField(Skill, related_name='users_with_skill', blank=True)
    social_links = models.TextField(blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name


class Project(models.Model):
    STATUS_CHOICES = (
        ('open', 'Открыт'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершён'),
        ('cancelled', 'Отменён'),
    )

    title = models.CharField(max_length=128)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_projects')
    skills_required = models.ManyToManyField(Skill, related_name='projects_with_skill')
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Offer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_offers')
    freelancer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='freelancer_offers')
    message = models.TextField()
    proposed_budget = models.DecimalField(max_digits=10, decimal_places=2)
    proposed_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.freelancer}, {self.project}'


class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_reviews')
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='given_reviews')
    target = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_reviews')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.reviewer}, {self.target}, {self.rating}'
