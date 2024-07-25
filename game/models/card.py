from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from game.models.player import Player


class CardColor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "game_card_color"


class CardElement(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "game_card_element"


class CardPower(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "game_card_power"


class Card(models.Model):
    color = models.ForeignKey(CardColor, on_delete=models.CASCADE)
    element = models.ForeignKey(CardElement, on_delete=models.CASCADE)
    power = models.ForeignKey(CardPower, on_delete=models.CASCADE, null=True, blank=True,
                              help_text="A special power of the card")
    value = models.IntegerField(default=2, validators=[MinValueValidator(2), MaxValueValidator(12)])
    players = models.ManyToManyField(Player, through="PlayerCard")

    def __str__(self):
        return f"[id {self.id}] {self.color} {self.element} {self.value}"


class PlayerCard(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.IntegerField("quantity of cards", default=1)

    class Meta:
        db_table = "game_player_card"


class CardStarterDeck(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = "game_card_starter_deck"
