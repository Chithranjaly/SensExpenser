import pytest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@pytest.mark.django_db
def test_user_authentication():
    # Create a test user
    user = User.objects.create_user(username='testuser', password='testpass')
    
    # Test authentication
    authenticated_user = authenticate(username='testuser', password='testpass')
    
    assert authenticated_user is not None
    assert authenticated_user.username == 'testuser'
    assert authenticated_user.is_authenticated
    
    # Clean up
    user.delete()
