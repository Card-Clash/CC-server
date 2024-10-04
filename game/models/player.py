from random import choice
from xmlrpc.client import DateTime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone


class Player(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    coins = models.IntegerField(default=0)
    permanent_ban = models.BooleanField(default=False, help_text="If this player has a permanent ban")
    discord_id = models.PositiveBigIntegerField(help_text="Identification number of the player in Discord")
    email = models.EmailField("email address")
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text=
        "Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts.",
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "players"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Email this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def ban(self, *, permanent: bool = False, issued: DateTime = None, expires: DateTime = None, moderator=None,
            reason: str = None):
        from game.models import Ban

        if permanent:
            self.permanent_ban = True
        else:
            Ban.objects.create(
                player=self,
                issued=issued,
                expires=expires,
                moderator=moderator,
                reason=reason,
            )

    def add_card(self, *, card, quantity: int = 1):
        if card in self.card_set.all():
            player_card = self.playercard_set.get(card=card)
            player_card.quantity += quantity
            player_card.save()
        else:
            self.card_set.add(card, through_defaults={"quantity": quantity})

    def draw_card(self):
        personal_deck = []
        for player_card in self.playercard_set.all():
            for _ in range(player_card.quantity):
                personal_deck.append(player_card.card)
        return choice(personal_deck)

    def __str__(self):
        return self.username

    def to_json(self) -> str:
        return str({"id": self.id, "username": self.username, "is_staff": self.is_staff, "is_active": self.is_active,
                    "coins": self.coins, "permanent_ban": self.permanent_ban, "date_joined": self.date_joined})
