from django.db import models
from django.contrib.auth.models import User

class Suggestion(models.Model):
    CATEGORY_CHOICES = [
        ('feedback', 'Feedback'),
        ('idea', 'Idea'),
        ('issue', 'Issue'),
    ]

    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('reviewed', 'Reviewed'),
    ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    is_anonymous = models.BooleanField(default=True)
    submitted_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
