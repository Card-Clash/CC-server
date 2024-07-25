from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from game.models.player import Player


def validate_staff(player_id: int):
    if not Player.objects.get(id=player_id).is_staff:
        raise ValidationError(
            "%(player)s is not a staff player.",
            params={"player": Player.objects.get(id=player_id).username},
        )


class Ban(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    issued = models.DateTimeField(default=timezone.now)
    expires = models.DateTimeField(default=timezone.now)
    moderator = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='moderators',
                                  help_text="Moderator who banned a player", validators=[validate_staff])
    reason = models.TextField()
