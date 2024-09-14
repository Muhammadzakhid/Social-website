import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from .models import Action


def created_action(user, verb, terget=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(
        user_id=user.id,
        
    )