from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    category_name = models.CharField(max_length=200)
    description = models.TextField(max_length=400, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user","category_name"],
                name='unique_user_category'
            )
        ]
    def __str__(self):
        return f"{self.category_name} ({self.user.username})"

# doubt regarding adding category to filter out, in serializer!!!!