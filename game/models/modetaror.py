from django.db import models
from django.utils import timezone

from game.models.player import Player


class Ban(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    issued = models.DateTimeField(default=timezone.now)
    expires = models.DateTimeField(default=timezone.now)
    moderator = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='moderators',
                                  help_text="Moderator who banned a player")
    reason = models.TextField()
