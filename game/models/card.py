from django.db import models

from game.models.player import Player


class CardColor(models.Model):
    name = models.CharField(max_length=50)


class CardElement(models.Model):
    name = models.CharField(max_length=50)


class CardPower(models.Model):
    name = models.CharField(max_length=50)


class Card(models.Model):
    color = models.ForeignKey(CardColor, on_delete=models.CASCADE)
    element = models.ForeignKey(CardElement, on_delete=models.CASCADE)
    power = models.ForeignKey(CardPower, on_delete=models.CASCADE, null=True)
    value = models.IntegerField(default=2)


class PlayerCard(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class CardStarterDeck(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
